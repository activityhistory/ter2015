__author__ = 'maxime'
import db_BaseClass
import os

class db_PrivacyKeywords(db_BaseClass.db_Base):

    def __init__(self, dbname):
        db_BaseClass.db_Base.__init__(self, dbname)
        self.tableName = "privacy_keywords"

    def getAll(self):

        keywords = []

        self.connect()
        #realy keywords
        for row in self.cursor.execute("SELECT keyword FROM privacy_keywords WHERE isApp == 0"):
            keywords.append(row[0])
        #unathorized app traited as keywords
        for row in self.cursor.execute("SELECT keyword FROM privacy_keywords WHERE isApp == 1 AND isprivate == 1"):
            keywords.append(row[0])

        self.disconnect()
        return keywords
