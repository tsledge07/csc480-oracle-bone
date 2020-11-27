'''
Author: Randolph Sapp
Info: Tool to rip images and transcript from bone script PDF
'''

import glob
import json
import os
from parser import Parser
import h5py
import cv2 as cv
from tablereader import TableReader

ROW_DESC = ['SectionHeader', 'CharNo', 'Script', 'ChnChar', 'Phonetic',
            'SpecimenNo', 'LCNo', 'Notes', 'SeqNo']
CARRY = [True, True, False, False, True, False, True, False, False]

for path in glob.glob("*.hdf5"):
    name = path[:-5]
    hdf5 = h5py.File(path, 'r')
    pdf = open(name+'.pdf', 'rb')
    pr = Parser(pdf)
    outputdir = name+'_output'
    os.makedirs(outputdir, exist_ok=True)
    oldelements, oldtranscript = [], {}
    ARI = 0
    for key, _ in enumerate(hdf5.keys()):
        page = hdf5[str(key)][()]
        tr = TableReader(page)
        pr.read_page(key)
        for ri in range(tr.numrows-1):
            row = tr.get_row(ri)
            rowdir = outputdir + '/' + str(ARI)
            os.makedirs(rowdir, exist_ok=True)
            transcript = {}
            for ci, element in enumerate(row):
                title = ROW_DESC[ci]
                x1, y1, x2, y2 = tr.get_cell_bounds(ri, ci)
                text = pr.get_text(x1, y1, x2, y2)
                if len(text) > 0:
                    transcript[title] = pr.get_text(x1, y1, x2, y2)
                elif CARRY[ci]:
                    transcript[title] = oldtranscript[title]
                if tr.is_cell_empty(ri, ci) and CARRY[ci]:
                    element = oldelements[ci]
                    row[ci] = element
                cv.imwrite(rowdir+'/'+title+'.png', element)
            json.dump(transcript, open(rowdir+'/transcript.json', 'w'))
            oldelements, oldtranscript = row, transcript
            ARI += 1
