__author__ = 'maxime'
import db_BaseClass
import os

class db_PrivacyKeywords(db_BaseClass.db_Base):

    def __init__(self, dbname):
        db_BaseClass.db_Base.__init__(self, dbname)
        self.tableName = "processevent"

    def getAll(self):

        keywords = []

        self.connect()
        for row in self.cursor.execute("SELECT keyword FROM privacy_keywords"):
            keywords.append(row[0])
        self.disconnect()
        return keywords
