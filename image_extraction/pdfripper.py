#!/usr/bin/env python3

'''
Author: Randolph Sapp
Info: Tool to rip images and transcript from bone script PDF
'''

import glob
import json
import os
import cv2 as cv
from image_extraction.parser import Parser
from image_extraction.tablereader import TableReader

ROW_DESC = ['SectionHeader', 'CharNo', 'Script', 'ChnChar', 'Phonetic',
            'SpecimenNo', 'LCNo', 'Notes', 'SeqNo']
CARRY = [True, True, False, False, True, False, True, False, False]

PPATHS = [os.path.splitext(x)[0] for x in glob.glob('*.pdf')]

for path in glob.glob('*.pdf'):
    name = os.path.splitext(path)[0]
    if not os.path.isdir(name):
        continue
    pdf = open(path, 'rb')
    pr = Parser(pdf)
    outputdir = name+'-output'
    os.makedirs(outputdir, exist_ok=True)
    oldelements, oldtranscript = [], {}
    ARI = 0
    for pi, impath in enumerate(sorted(glob.glob(name+'/*.png'))):
        page = cv.imread(impath)
        tr = TableReader(page)
        pr.read_page(pi)
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
