# Author: Randolph Sapp
# Info: Tool to parse tables in PDFs

import numpy as np
import cv2 as cv

class tablereader:
    def __init__(self, page):
        self.dst = cv.cvtColor(page, cv.COLOR_BGR2GRAY)
        _, self.thresh = cv.threshold(self.dst, 200, 255, cv.THRESH_BINARY_INV)
        self.numrows = 0
        self.numcols = 0
        self.h_lines = []
        self.v_lines = []
        self.updateLines()

    def updateLines(self):
        lines = cv.HoughLinesP(self.thresh, 1, np.pi*0.5, 500, None, 500, 5)
        if lines is not None:
            for line in sorted(lines, key=lambda x:x[0][0]):
                x1, y1, x2, y2 = line[0]
                if self.numcols < 1 or abs(x1-self.v_lines[-1][0]) > 20:
                    self.v_lines.append([x1, y1, x2, y2])
                    self.numcols += 1
            for line in sorted(lines, key=lambda x:x[0][1]):
                x1, y1, x2, y2 = line[0]
                if self.numrows < 1 or abs(y1-self.h_lines[-1][1]) > 20:
                    self.h_lines.append([x1, y1, x2, y2])
                    self.numrows += 1

    def getCell(self, j, i):
        return self.thresh[self.h_lines[j][1]+5:self.h_lines[j+1][1]-2,
               self.v_lines[i][0]+5:self.v_lines[i+1][0]-2]

    def isEmpty(self, j, i):
        cell = self.getCell(j, i)
        return cell.size*0.01 > cv.countNonZero(cell)

    def getCellBounds(self, j, i):
        return [(self.v_lines[i][0]+5)/self.dst.shape[1], (self.h_lines[j][1]+5)/self.dst.shape[0],
                (self.v_lines[i+1][0]-2)/self.dst.shape[1], (self.h_lines[j+1][1]-2)/self.dst.shape[0]]

    def getRow(self, j):
        i = 0
        output = []
        while i < len(self.v_lines)-1:
            output.append(self.getCell(j, i))
            i += 1
        return output

