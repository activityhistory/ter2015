__author__ = 'maxime'

import db_BaseClass
import DateParser
import imageSetClass


class db_virtual_activeWindow(db_BaseClass.db_Base):
    """
    Virtual db table interface
    join processevent and process
    """
    def __init__(self, dbname):
        db_BaseClass.db_Base.__init__(self, dbname)

    def getTheActiveAppBySCSName(self, scsName):
        """
        Return the last "active" process name, just before tha date of the screenshot
        @param scsName: screenshot name : to have the date
        @return: the last active process
        """
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
        """
        Return the last active app of one iamgeSet
        Take the last imageSet screenshot to comparge dates
        @param imgset: ImageSet instance
        @return:The active app
        """
        #if the sequence is too short, it need to add a second and trucate
        if(len(imgset) <= 2):
            scsName = imgset.stop
            scsName = DateParser.addASecondAndTrucate(scsName)
            return self.getTheActiveAppBySCSName(scsName)

        return self.getTheActiveAppBySCSName(imgset.stop)


    def setTheActiveAppInImageSet(self, imgset):
        """
        Get the active ap (getTheActiveAppByImageSet) and set it in the imageSet
        @param imgset: ImageSet instance
        @return:None
        """

        imgset.setFocusedApp(self.getTheActiveAppByImageSet(imgset))


    def setTheActiveAppInAllImagesSet(self, imgsets):
        """
        Get and set into each imageSet of the list , the foccused app of each
        @param imgsets: ImageSet instance
        @return: None
        """
        for imgset in imgsets:
            self.setTheActiveAppInImageSet(imgset)
