__author__ = 'maxime'
import db_BaseClass
import os

class db_Location(db_BaseClass.db_Base):

    def __init__(self, dbname):
        db_BaseClass.db_Base.__init__(self, dbname)
        self.tableName = "location"


    def getLastLocationAtTime(self, db_time):
        """
        Return the last known location before the db_time
        @param db_time: time in db format
        @return: the last known location (latitude, longitude)
        """
        self.connect()
        res = self.cursor.execute("SELECT lat, lon FROM location WHERE created_at < '"+db_time+"' ORDER BY created_at DESC LIMIT 1").fetchone()
        self.disconnect()
        return (res[0], res[1])

