import DateParser

__author__ = 'maxime'

import db_Privacy_TimeClass

class FilterByTime:
    """
    Filter images by allowed (or not) times
    * take back the allowed times
    * filter

    """
    boolWeek = None
    boolWeekEnd = None
    hourStart = None
    hourStop = None
    minStart = None
    minStop = None


    def __init__(self, db):
        """
        Constructor
        Take back the filter times informations from db
        @param db: name and path of the db
        @return: None
        """
        data = db_Privacy_TimeClass.db_Privacy_Time(db).getTimeInfos()
        self.boolWeek = True if data['week'] == 1 else False
        self.boolWeekEnd = True if data['weekEnd'] == 1 else False
        self.hourStart = data['fromHour']
        self.hourStop = data['toHour']
        self.minStop = data['toMin']
        self.minStart = data['fromMin']


    def doFilterOnImgSetList(self, imgSetList):
        """
        Filter each imageSet on a imageSet array
        @param imgSetList: Array of imageSet instances
        @return: None
        """
        for imgset in imgSetList:
            self.doFilterOneImgSet(imgset)


    def doFilterOneImgSet(self, imgset):
        """
        Do filter on One ImageSet
        @param imgset: instance of ImageSet
        @return: True if the imageSet is in the time laps, False else
        """
        if(self.boolWeekEnd == False and self.boolWeek == False):
            self.badTime(imgset)
            return False
        if(self.boolWeekEnd == False and (self.isOnWeekEnd(imgset.start) or self.isOnWeekEnd(imgset.stop))):
            self.badTime(imgset)
            return False
        if(self.boolWeek == False and ((not self.isOnWeekEnd(imgset.start)) or (not self.isOnWeekEnd(imgset.stop)))):
            self.badTime(imgset)
            return False
        if((not self.isInTimeSlot(imgset.start)) or (not self.isInTimeSlot(imgset.stop))) :
            self.badTime(imgset)
            return False
        return True

    def badTime(self, imgset):
        """
        Set to the imageSet that it is on a bad time laps
        @param imgset:
        @return:
        """
        imgset.setUnAcceptable()
        imgset.addFiltredBy("Time")

    def isOnWeekEnd(self, scsName):
        """
        Know if a date (by screenshot name) is on weekend or not
        @param scsName: instance of iamgeSet
        @return:True if on the WE, False else
        """
        date = DateParser.getDateBySCS(scsName)
        weekend = set([5,6])
        if date.weekday() not in weekend :
            return False
        else :
            return True


    def isInTimeSlot(self, scsName):
        """
        Know if a date (by screenshot name) os in the time slot (laps...)
        @param scsName: name of the Screenshot (to have the date)
        @return: True if teh date is inside the time laps, False else.
        """
        date = DateParser.getDateBySCS(scsName)
        #hour
        if(date.hour < self.hourStart or date.hour > self.hourStop):
            return False
        #min
        if(
                (date.hour == self.hourStart and date.minute < self.minStart)
                or
                    (date.hour == self.hourStop and date.minute > self.minStop)):
            return False
        return True
