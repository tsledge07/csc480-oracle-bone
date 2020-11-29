#!/usr/bin/env python3

'''
Author: Randolph Sapp
Info: Tool to parse tables in PDFs
'''

import glob
import os
from pdf2image import convert_from_path

for path in glob.glob("*.pdf"):
    name = path[:-4]
    os.makedirs(name, exist_ok=True)
    convert_from_path(path, dpi=300, output_folder=name, use_pdftocairo=True,
                      output_file='', fmt='png', thread_count=4)
