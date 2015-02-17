__author__ = 'maxime'

import imageSetClass
import os

class Cleaner:

    imgset = None
    scsPath = None
    txtPath = None

    def __init__(self, imgset, scsPath, txtPath):
        self.imgset = imgset
        self.scsPath = scsPath
        self.txtPath = txtPath

    def clean(self):
        self.cleanOCRed()
        self.cleanScreenshots()

    def cleanScreenshots(self):
        lst = self.imgset.getSortedImagesList()
        nb = 0
        for file in lst:
            if os.path.isfile(self.scsPath+file):
                os.remove(self.scsPath+file)
                nb += 1
        return nb

    def cleanOCRed(self):
        lst = self.getOCRedTextFilesListBySCSList()
        nb = 0
        for file in lst:
            if os.path.isfile(self.txtPath+file):
                os.remove(self.txtPath+file)
                nb += 1
        return nb


    def getOCRedTextFilesListBySCSList(self):
        OCRDFiles = []
        for file in self.imgset.getSortedImagesList():
            OCRDFiles.append(file.split(".")[0]+".txt")
        return OCRDFiles

