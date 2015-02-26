__author__ = 'maxime'
import os
import glob
import json

import DateParser


class imageSet:
    """
    ImageSet : represent a suit of images
    with some attributes :
    if acceptable or not
    the OCRed text, location (and user name), times, foccused ap ...
    """

    start = None
    stop = None
    relativePath = None
    acceptable = None
    OCRedText = None
    location = None
    focusedApp = None
    startTime = None
    stopTime = None
    length = None
    locationName = None
    filtredBy = None

    def __init__(self, start, stop, relativePath):
        """
        Constructor
        Need the start and stop screenshot name, and their path
        @param start: name of the screenshot that start the imageSet indluded
        @param stop: name of te screenshoty that end the imageSet INCLUDED
        @param relativePath: the path of the screenshot folder
        @return: None
        """
        self.relativePath = relativePath
        if(self.checkImageExist(start) and self.checkImageExist(stop)):
            self.start = start
            self.stop = stop
        else:
            raise Exception("Start and/or stop files doesn't exist : "+ start +" or "+stop+" at : "+ relativePath)
        self.startTime = str(DateParser.SCStoDB(start))
        self.stopTime = str(DateParser.SCStoDB(stop))
        self.length = len(self)
        self.acceptable = True
        self.locationName = None
        self.filtredBy = []

    def getRelativePath(self):
        return self.relativePath

    def setAcceptable(self):
        self.acceptable = True

    def setUnAcceptable(self):
        self.acceptable = False

    def checkImageExist(self, imageName):
        """
        Verify if screenshots exists
        @param imageName:
        @return:
        """
        imgPath = os.path.join(self.relativePath, imageName)
        return os.path.isfile(imgPath)

    def getStartWithPath(self):
        return os.path.join(self.relativePath, self.start)

    def getStopWithPath(self):
        return os.path.join(self.relativePath, self.stop)

    def getSortedImagesList(self):
        """
        @return: the image list included in this image set, with path
        """
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

    def setOCRedText(self, txt):
        self.OCRedText = txt

    def getOCRedText(self):
        return self.OCRedText

    def setLocation(self, lat, long):
        self.location = (lat, long)

    def getLocation(self):
        return self.location

    def setFocusedApp(self, fcapp):
        self.focusedApp = fcapp

    def getFocusedApp(self):
        return self.focusedApp

    def addFiltredBy(self, bywhat):
        self.filtredBy.append(bywhat)

    def __len__(self):
        return len(self.getSortedImagesList())

    def __str__(self):
        return "Image set :" \
               "\nStart : " + str(self.start) \
               + "\nStop : " + str(self.stop) \
               + "\nAcceptable : " + str(self.acceptable) \
               + "\nNombre d'images :" + str(len(self)) \
               + "\nLocation : "+ str(self.location) \
               +"\nFoccusedApp : "+str(self.focusedApp)\
               +"\\nOCRedText : " +str( self.OCRedText)


class imageSetEncoder(json.JSONEncoder):
    """
    Enode to JSON an ImageSet instance
    """
    def default(self, o):
        if not isinstance(o, imageSet):
            return super(imageSetEncoder, self).default(o)
        return o.__dict__
