__author__ = 'maxime'
import db_BaseClass
import os

class db_Process(db_BaseClass.db_Base):

    def __init__(self, dbname):
        db_BaseClass.db_Base.__init__(self, dbname)
        self.tableName = "process"


    def getNotAllowedAppList(self):
        """
        Return the list off apps that user said it is private usage apps
        @return: array of strings : name of not allowed apps
        """
        lst = []
        self.connect()
        for row in self.cursor.execute("SELECT name FROM process WHERE isprivate == 1"):
            lst.append(row[0].decode('utf-8'))
        self.disconnect()
        return lst