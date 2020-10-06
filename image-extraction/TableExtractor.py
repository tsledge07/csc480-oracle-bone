# Author: Randolph Sapp
# Info: Tool to parse tables in PDFs

import glob
import h5py
import numpy as np
import cv2 as cv

def getLines(page):
    dst = cv.cvtColor(page, cv.COLOR_BGR2GRAY)
    _,thresh1 = cv.threshold(dst,220,255,cv.THRESH_BINARY_INV)
    lines = cv.HoughLinesP(thresh1, 1, np.pi*0.5, 500, None, 500, 5)
    horizontal_lines = []
    vertical_lines = []
    if lines is not None:
        for line in sorted(lines, key=lambda x:x[0][0]):
            x1, y1, x2, y2 = line[0]
            if len(vertical_lines) < 1 or abs(x1-vertical_lines[-1][0]) > 20:
                vertical_lines.append([x1,y1,x2,y2])
        for line in sorted(lines, key=lambda x:x[0][1]):
            x1, y1, x2, y2 = line[0]
            if len(horizontal_lines) < 1 or abs(y1-horizontal_lines[-1][1]) > 20:
                horizontal_lines.append([x1,y1,x2,y2])
    return (horizontal_lines, vertical_lines)

for path in glob.glob("*.hdf5"):
    hdf5 = h5py.File(path, 'r')
    for i, _ in enumerate([0]):#hdf5.keys()):
        page = hdf5[str(i)][()]
        hlines,vlines = getLines(page)
        xs = []
        ys = []
        for line in hlines:
            ys.append(line[1])
        for line in vlines:
            xs.append(line[0])

        for j in range(len(ys)-1):
            for i in range(len(xs)-1):
                cv.imshow("Source", page[ys[j]+2:ys[j+1]+2, xs[i]+2:xs[i+1]+2])
                cv.waitKey()


#cv.imshow("Source", page)
#cv.waitKey()
