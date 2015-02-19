import DateParser

__author__ = 'maxime'



class FilterByTime:

    boolWeek = None
    boolWeekEnd = None
    hourStart = None
    hourStop = None
    minStart = None
    minStop = None


    def __init__(self):
        #here take back the allowed times to record
        self.boolWeek = True
        self.boolWeekEnd = False
        self.hourStart = 9
        self.hourStop = 17
        self.minStart = 30
        self.minStop = 30


    def doFilterOnImgSetList(self, imgSetList):
        for imgset in imgSetList:
            self.doFilterOneImgSet(imgset)


    def doFilterOneImgSet(self, imgset):
        if(self.boolWeekEnd == False and self.boolWeek == False):
            imgset.setUnAcceptable()
            return False
        if(self.boolWeekEnd == False and (self.isOnWeekEnd(imgset.start) or self.isOnWeekEnd(imgset.stop))):
            imgset.setUnAcceptable()
            return False
        if(self.boolWeek == False and ((not self.isOnWeekEnd(imgset.start)) or (not self.isOnWeekEnd(imgset.stop)))):
            imgset.setUnAcceptable()
            return False
        if((not self.isInTimeSlot(imgset.start)) or (not self.isInTimeSlot(imgset.stop))) :
            imgset.setUnAcceptable()
            return False
        return True

    def isOnWeekEnd(self, scsName):
        date = DateParser.getDateBySCS(scsName)
        weekend = set([5,6])
        if date.weekday() not in weekend :
            return False
        else :
            return True


    def isInTimeSlot(self, scsName):
        date = DateParser.getDateBySCS(scsName)
        print date.hour
        print date.minute
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
