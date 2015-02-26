__author__ = 'maxime'

import imageSetClass
import os
import db_BookmarkClass
import db_ClickClass
import db_GeometryClass
import db_KeysClass
import db_ProcessEventClass
import db_RecordingEventClass
import db_WindowClass
import db_WindowEventClass
import DateParser


class Cleaner:
    """
    Class Cleaner
    Clean every data recorded in ActivityHistory project between two dates. included :
        * Screenshots
        * OCRed Texts
        * Database data
    Usage :
    cleaner = Cleaner(imagesSet, Path_to_screenshot_folder, Path_to_OCRed_Text_Filder, Path_And_Name_Of_The_DB)
    cleaner.clean() # clean all
    """

    imgset = None
    scsPath = None
    txtPath = None
    db = None

    def __init__(self, imgset, scsPath, txtPath, db):
        """
        Constructor
        @param imgset: The imageSet to delete informations
        @param scsPath: the path of the screenshot folder
        @param txtPath: the path of the OCRed Text forlder
        @param db: the path and the name of the database
        @return: None
        """
        self.imgset = imgset
        self.scsPath = scsPath
        self.txtPath = txtPath
        self.db = db

    def clean(self):
        """
        Execute cleaning :
            * Screenshots
            * OCRed Texts
            * Database data
        @return:None
        """
        self.cleanOCRed()
        self.cleanDB()
        self.cleanScreenshots()

    def cleanScreenshots(self):
        """
        Clean (Delete) the screenshots of the imageSet
        @return:None
        """
        lst = self.imgset.getSortedImagesList()
        nb = 0
        for file in lst:
            if os.path.isfile(self.scsPath+file):
                os.remove(self.scsPath+file)
                nb += 1
        return nb

    def cleanOCRed(self):
        """
        Clean (delete) the text files (OCRed text) mathing the imageset time slot
        @return:
        """
        lst = self.getOCRedTextFilesListBySCSList()
        nb = 0
        for file in lst:
            if os.path.isfile(self.txtPath+file):
                os.remove(self.txtPath+file)
                nb += 1
        return nb


    def getOCRedTextFilesListBySCSList(self):
        """
        Take back the OCRed text file mathing the image set to clean.
        @return:the text files list (array)
        """
        OCRDFiles = []
        for file in self.imgset.getSortedImagesList():
            OCRDFiles.append(file.split(".")[0]+".txt")
        return OCRDFiles

    def cleanDB(self):
        """
        Clean all db entries during the time slot mathcing the imageSet.
        included :
            * bookmarks
            *click
            *geometry
            *keys
            *processEvent
            *RecordingEvents
            *Window
            *windoevent
        @return: None
        """
        start = DateParser.SCStoDB(self.imgset.start)
        stop = DateParser.SCStoDB(self.imgset.stop)

        print db_BookmarkClass.db_Bookmark(self.db).deleteFromTo(start, stop)
        print db_ClickClass.db_Click(self.db).deleteFromTo(start, stop)
        print db_GeometryClass.db_Geometry(self.db).deleteFromTo(start, stop)
        print db_KeysClass.db_Keys(self.db).deleteFromTo(start, stop)
        print db_ProcessEventClass.db_ProcessEvent(self.db).deleteFromTo(start, stop)
        print db_RecordingEventClass.db_RecordingEvent(self.db).deleteFromTo(start, stop)
        print db_WindowClass.db_Window(self.db).deleteFromTo(start, stop)
        print db_WindowEventClass.db_Windowevent(self.db).deleteFromTo(start, stop)
