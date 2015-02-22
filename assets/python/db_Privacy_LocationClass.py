__author__ = 'maxime'
import db_BaseClass
import os

class db_Privacy_Location(db_BaseClass.db_Base):

    def __init__(self, dbname):
        db_BaseClass.db_Base.__init__(self, dbname)
        self.tableName = "privacy_locations"


    def getUserLocationList(self):
        self.connect()
        res = []
        for row in self.cursor.execute("SELECT longitude, latitude FROM privacy_locations"):
            res.append((row[0], row[1]))
        self.disconnect()
        return res

    #TODO : no response case
    def isAPrivateLocation(self, lat, long):
        self.connect()
        res = self.cursor.execute("SELECT isprivate FROM privacy_locations WHERE longitude LIKE '"+str(long)+"%' AND latitude LIKE '"+str(lat)+"%'").fetchone()
        self.disconnect()
        if(res[0] == 1):
            return True
        else:
            return False

    #TODO: no response case
    def getLocationUserName(self, lat, long):
        self.connect()
        res = self.cursor.execute("SELECT name FROM privacy_locations WHERE longitude LIKE '"+str(long)+"%' AND latitude LIKE '"+str(lat)+"%'").fetchone()
        self.disconnect()
        return res[0]


# db = db_Privacy_Location("../../selfspy.sqlite")
# lst = db.getUserLocationList()
# (long, lat) = lst[0]
# print str(db.isAPrivateLocation(lat, long))
# print str(db.getLocationUserName(lat, long))