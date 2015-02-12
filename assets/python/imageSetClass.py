__author__ = 'maxime'
import os
import glob

class imageSet:
    """
    ImageSet : represent a suit of images
    with some attributes :
    if acceptable or not
    the OCRed text
    """

    def __init__(self, start, stop, relativePath):
        self.relativePath = relativePath
        if(self.checkImageExist(start) and self.checkImageExist(stop)):
            self.start = start
            self.stop = stop
        else:
            raise Exception("Start and/or stop files doesn't exist : "+ start +" or "+stop+" at : "+ relativePath)

    def setAcceptable(self):
        self.acceptable = True

    def setUnAcceptable(self):
        self.acceptable = False

    def checkImageExist(self, imageName):
        imgPath = os.path.join(self.relativePath, imageName)
        return os.path.isfile(imgPath)

    def getStartWithPath(self):
        return os.path.join(self.relativePath, self.start)

    def getStopWithPath(self):
        return os.path.join(self.relativePath, self.stop)

    def getSortedImagesList(self):
        allFiles = glob.glob(os.path.join(self.relativePath, "*.jpg"))
        allFiles.sort()

        lstImg = []

        current = 0
        while(allFiles[current] != self.getStartWithPath() and current < (len(allFiles)-1) ):
            current +=1
        while(allFiles[current] != self.getStopWithPath() and current < (len(allFiles)-1) ):
            lstImg.append(os.path.basename(allFiles[current]))
            current += 1
        lstImg.append(self.stop)
        return lstImg

    def __len__(self):
        return len(self.getSortedImagesList())

    def __str__(self):
        return "start : " + self.start + "\nstop : " + self.stop + "\n Acceptable : " + str(self.acceptable) + "\nNombre d'images :" + str(len(self))



