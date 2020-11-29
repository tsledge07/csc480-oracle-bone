import cv2 as cv
import h5py
import glob

for path in glob.glob("*.hdf5"):
    hdf5 = h5py.File(path, 'r')
    for i, _ in enumerate([0]): #hdf5.keys()):
        page = hdf5[str(i)][()]
        tr = tablereader(page)
        cv.imshow("Source", tr.getCell(1, 2))
        cv.waitKey()
