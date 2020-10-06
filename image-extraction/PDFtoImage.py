# Author: Randolph Sapp
# Info: Tool to parse tables in PDFs

import glob
import h5py
import re
from pdf2image import convert_from_path

for path in glob.glob("*.pdf"):
    name = path[:-4]
    hdf5 = h5py.File(name+'.hdf5', 'w')
    images = convert_from_path(path, dpi=800)
    for i, page in enumerate(images):
        hdf5[str(i)] = page
