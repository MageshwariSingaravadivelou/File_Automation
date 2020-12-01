# File Automation

File Automation is a Windows Desktop application created using Python that will read various input files and append the data to respective base files.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) and  [conda](https://docs.conda.io/projects/conda/en/latest/commands/install.html) to install the required packages

```bash
conda install -c anaconda tk
conda install -c conda-forge pyinstaller
conda install -c anaconda pywin32
pip install pyinstaller
```

## Usage
To convert the python file to executable (.exe) file use the below command.
```Anaconda Prompt

pyinstaller --onefile <file_name>.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
