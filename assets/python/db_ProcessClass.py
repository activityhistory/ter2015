__author__ = 'maxime'
import db_BaseClass
import os

class db_Process(db_BaseClass.db_Base):

    def __init__(self, dbname):
        db_BaseClass.db_Base.__init__(self, dbname)
        self.tableName = "process"

    def getAll(self):

        keywords = []

        self.connect()
        for row in self.cursor.execute("SELECT keyword FROM process"):
            keywords.append(row[0])
        self.disconnect()
        return keywords


    def getNotAllowedAppList(self):
        lst = []
        self.connect()
        for row in self.cursor.execute("SELECT name FROM process WHERE isprivate == 1"):
            lst.append(row[0].decode('utf-8'))
        self.disconnect()
        return lst