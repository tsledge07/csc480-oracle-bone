# Image Processing Utilities
A set of tools developed to extract and process PDF tables and associated transcripts.

NOTE:
 - These utilities are optimized for the Oracle Bone PDFs
 - All paths mentioned with `.` are relative to the directory containing this README
 - Extensions are case sensitive on some OSs, this utility expects them to be lowercase

## Installation
It is recommended to install this package in development mode so modifications take effect immediately. In addition to this, it's also recommended to install this package through Anaconda in Windows unless you want to resolve the poppler dependency yourself.
This can be done with either:
```
python setup.py develop
```
or
```
pip install -e .
```
Dependencies should be automatically resolved, but in case they aren't required dependencies are also listed in `./requirements.txt`

## Testing
This package takes advantage of the UnitTest library for automated unit testing of the 2 extraction classes. To run these tests navigate to the `./tests` directory and run either `python test_parser.py` or `python test_tablereader.py`. Additionally you may run all tests with `python -m unittest discover` in the `./tests` directory. Regardless way all tests should be run in the `./tests` directory.

## Usage
This package has three distinct processing steps that are split up to allow for easy modification. These commands are to be ran in the directory containing all PDFs that are to be processed.

### Pre-processing
Image arrays must be generated and stored ahead of time due to the intense resource usage. This is out of my control and must be done for the computer vision side of this utility. This is done by running `pdfpreproc.py`. By default we export the PDF at a respectable 300 DPI but this can be changed in `./pdfpreproc.py`. This will affect processing time and all generated file sizes so adjust this parameter sparingly.

### Processing
Simply run `pdfproc.py` in the directory containing the PDFs and their corresponding `*-pre` image directories you wish to extract. All available PDF-DIR pairs in this directory will be processed with the rules outlined in `./pdfproc.py`. All images generated will be stored in a `*-proc` directory tree.

### Post-processing
After extracting the required cells you may wish to perform some thinning or other processing routines on the directory tree generated. This utility has a tool to traverse these trees and do so automatically. Running `pdfpostproc.py` will perform the processing routines outlined in `./pdfpostproc.py` on any `*-proc` subdirectories in the current working directory. The output will be saved into a separate directory tree by default. Right now the images are binarized (all pixels either being 0 or 255) and thinned before being stored in the `*-proc` directory tree. If you don't want to export these images into a seperate tree simple change the `outpath` variable

### Cleanup
If you don't need to reread the PDF over and over then you may delete the `*-pre` directories to save space.
