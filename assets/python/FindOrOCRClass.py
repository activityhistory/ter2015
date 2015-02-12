__author__ = 'maxime'

import os
import OCR


class FindOrOCR:

    def __init__(self, screenshotsRelativePath, textsRelativePath):
        self.scsPath = screenshotsRelativePath
        self.textsPath = textsRelativePath


    def getText(self, screenshotName, save=True):
        #check scs
        txt = self.getTextByText(screenshotName)
        if(txt != -1) :
            return txt
        else :
            txt = self.getTextByOCR(screenshotName)
            if(save) :
                self.saveNewTxt(screenshotName, txt)
            return txt


    def saveNewTxt(self, screenshotName, txt):
        #making the path
        txtPath = os.path.join(self.textsPath, screenshotName)
        (txtPath, ext) = os.path.splitext(txtPath)
        txtPath += ".txt"
        ficTxt = open(txtPath, "w")
        ficTxt.write(txt)
        ficTxt.close()


    def getTextByText(self, screenshotName):

        #making the path
        txtPath = os.path.join(self.textsPath, screenshotName)
        (txtPath, ext) = os.path.splitext(txtPath)
        txtPath += ".txt"

        #check if the file exist
        if(os.path.exists(txtPath)):
            file = open(txtPath, "r")
            txt = file.read()
            file.close()
            return txt
        else:
            return -1

    def getTextByOCR(self, screenshotName):

        #making the path
        scsPath = os.path.join(self.scsPath, screenshotName)
        return OCR.OCR_SCS(scsPath)
