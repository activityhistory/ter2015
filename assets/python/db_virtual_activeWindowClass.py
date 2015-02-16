__author__ = 'maxime'

import db_BaseClass
import DateParser
import imageSetClass


class db_virtual_activeWindow(db_BaseClass.db_Base):

    def __init__(self, dbname):
        db_BaseClass.db_Base.__init__(self, dbname)

    def getTheActiveAppBySCSName(self, scsName):
        scsDate = scsName.split(".")[0] # remove the ext
        date = DateParser.SCStoDB(scsDate)
        query = "SELECT name, processevent.created_at FROM process" \
                                       +" INNER JOIN processevent ON processevent.process_id = process.id" \
                                       +" WHERE processevent.event_type = 'Active' AND processevent.created_at" \
                                       +" <= '"+date+"%' ORDER BY processevent.created_at DESC LIMIT 1;"
        self.connect()
        r = None
        for row in self.cursor.execute(query):
            r = row[0]
        self.disconnect()
        return r


    def getTheActiveAppByImageSet(self, imgset):
        #if the sequence is too short, it need to add a second and trucate
        if(len(imgset) <= 2):
            scsName = imgset.stop
            scsName = DateParser.addASecondAndTrucate(scsName)
            return self.getTheActiveAppBySCSName(scsName)

        return self.getTheActiveAppBySCSName(imgset.stop)


    def setTheActiveAppInImageSet(self, imgset):
        imgset.setFocusedApp(self.getTheActiveAppByImageSet(imgset))


    def setTheActiveAppInAllImagesSet(self, imgsets):
        for imgset in imgsets:
            self.setTheActiveAppInImageSet(imgset)
