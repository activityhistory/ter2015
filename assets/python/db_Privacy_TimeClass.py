__author__ = 'maxime'
import db_BaseClass
import os

class db_Privacy_Time(db_BaseClass.db_Base):

    def __init__(self, dbname):
        db_BaseClass.db_Base.__init__(self, dbname)
        self.tableName = "privacy_locations"

    #TODO : no data case
    def getTimeInfos(self):
        self.connect()
        res = self.cursor.execute("SELECT * FROM privacy_time LIMIT 1").fetchone()
        self.disconnect()
        return {"weekEnd": res[1], "week": res[2], "fromHour": int(res[3].split(":")[0]), "fromMin": int(res[3].split(":")[1]), "toHour": int(res[4].split(":")[0]), "toMin": int(res[4].split(":")[1])}
