import argparse
import gzip
import requests
from collections import Counter
from io import BytesIO
from http import HTTPStatus


class Contentfiles:

    """ Class to download, parse and display statistics of Debian package files
        Attributes:
                architecture (str): Target architecture
                mirror (str): The Debian mirror URL
    """

    def __init__(self, architecture):
        """
            Initializes class with architecture and set mirror url.
        """

        self.architecture = architecture
        self.mirror = (
            f"http://ftp.uk.debian.org/debian/dists/stable/main/"
            f"Contents-{architecture}.gz"
        )

    def download_contents(self):
        """
            Downloads the compressed Contents file from the
            Debian mirror and parses its contents.
        """

        # Download the compressed Contents file
        response = requests.get(self.mirror)
        #Checking if response status not OK
        if response.status_code != HTTPStatus.OK:
            # File cannot be downloaded error handled
            print("Failed to download file.")
            return None
        # Open downloaded gzip file in text mode and parse contents
        with gzip.open(BytesIO(response.content), 'rt') as f:
            return self.parse_contents(f)

    def parse_contents(self, file_content):
        """
            Handles parsing of Contents file and file count per package
        """

        # Parse the content of the Contents file and count files per package
        package_files_counter = Counter()
        for line in file_content:
            parts = line.strip().split()
            # Check if the line has at least two parts
            if len(parts) < 2:
                continue
            # Extract package names from the last part of the line
            package_names = parts[-1].split(',')

            for package_name in package_names:
                package_files_counter[package_name] += 1
        return package_files_counter

    def display_stats_top10_packages(self, top_n=10):
        """
            Displays statistics of the top 10 packages
            having the most files associated with them
        """

        package_files_counter = self.download_contents()
        if not package_files_counter:
            return
        # Enumerate and print the top 10 packages
        for index, (package, count) in enumerate(
            package_files_counter.most_common(top_n), start=1
        ):
            print(f"{index if index >= 10 else ' ' + str(index)}."
                  f" {package:<30}  {count:>10}")


if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Debian Package Statistics')
    parser.add_argument('architecture', help='Architecture type')
    args = parser.parse_args()
    # Create an instance of the ContentFiles class
    stats_tool = Contentfiles(args.architecture)
    # Display the stats for the top 10 packages
    stats_tool.display_stats_top10_packages()
