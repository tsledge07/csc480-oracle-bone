# Image Processing Utilities
A set of tools developed to extract and process PDF tables and associated transcripts.

NOTE:
 - These utilities are optimized for the Oracle Bone PDFs
 - All paths mentioned with `.` are relative to the directory containing this README
 - Extensions are case sensitive on some OSs, this utility expects them to be lowercase

## Installation
It is recommended to install this package in development mode so modifications take effect immediately. In addition to this it's recommended to install this in Anaconda in Windows unless you want to resole the poppler dependency yourself.
This can be done with either:
```
python setup.py develop
```
or
```
pip install -e .
```
Dependencies should be automatically resolved, but in case they aren't required dependencies are also listed in `./requirements.txt`

## Usage
This package has three distinct processing steps that are split up to allow for easy modification. These commands are to be ran in the directory containing all PDFs that are to be processed.

### Pre-processing
Image arrays must be generated and stored ahead of time due to the intense resource usage. This is out of my control and must be done for the computer vision side of this utility. This is done by running `pdfpreproc.py`. By default we export the PDF at a respectable 300 DPI but this can be changed in `./pdfpreproc.py`. This will affect processing time and all generated file sizes so adjust this parameter sparingly.

### Processing
Simply run `pdfproc.py` in the directory containing the PDFs and their corresponding image directories you wish to extract. All available PDF-DIR pairs in this directory will be processed with the rules outlined in `./pdfproc.py`.

### Post-processing
After extracting the required cells you may wish to perform some thinning or other processing routines on the directory tree generated. This utility has a tool to traverse these trees and do so automatically. Running `pdfpostproc.py` will perform the processing routines outlined in `./pdfpostproc.py` on any `*-output` subdirectories in the current working directory.

