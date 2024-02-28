# CLI_tool
python command line tool that takes the architecture (amd64, arm64, mips, etc.) as an argument and downloads the compressed Contents file associated with it from a Debian mirror. The program should parse the file and output the statistics of the top 10 packages that have the most files associated with them.

## Dependencies Installation
It is expected that Python (version 3.0 preferred) is installed.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages such as argparse, gzip, requests, and collections.

```bash
pip install -r requirements.txt
```

## Usage 
Run the command below to run the CLI tool replacing architecture with (amd64, arm64, mips, etc.) 
```python
python3 package_statistics.py <architecture>
```
Example command using the amd64
```python
python3 package_statistics.py amd64
```
## Approach
To develop the command line tool my approach was to first construct the URL from the Debian mirror to download the compressed Contents file corresponding to the architecture passed as an argument. The next step is to download this file using the requests gzip library and to decompress it in-memory using gzip and BytesIO respectively. Moving on to parsing the decompressed data to count the number of files associated with each package by using the Counter class from the collections module to efficiently count occurrences. Lastly, sort these counts in descending order and print out the top 10 packages with the most files. The code is written to be executed from the command line, by setting up the command line argument parsing accepting the architecture type as an argument. 

Additionally, I used flake8 to ensure the code is compliant, mentioned inline comments where required, and also used Docstrings to document the usage of the class and respective functions. Also, I implemented the functions within a class for better organization following Python's best practices. 

##Time taken
This task took around 3hrs including logic building, implementation, testing and checking for compliance.
