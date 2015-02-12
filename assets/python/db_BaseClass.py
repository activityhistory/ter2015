__author__ = 'maxime'

import sqlite3


class db_Base:

    connection = None
    cursor = None

    def __init__(self, databaseName):
        self.databaseName = databaseName


    def connect(self):
        self.connection = sqlite3.connect(self.databaseName)
        self.cursor = self.connection.cursor()

    def commit(self):
        self.c

    def disconnect(self):
        self.cursor.close()

    def __del__(self):
       if(self.connection != None):
           self.disconnect()
