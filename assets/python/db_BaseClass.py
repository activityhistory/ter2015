__author__ = 'maxime'

import sqlite3


class db_Base:
    """
    The commun database class, inherited by each database class
    define basics functions : connect, commit, disconnect
    Define also a "delete from ... to ..." function, used by the cleaner to each tables
    """

    connection = None
    cursor = None
    tableName=None

    def __init__(self, databaseName):
        self.databaseName = databaseName


    def connect(self):
        self.connection = sqlite3.connect(self.databaseName)
        self.cursor = self.connection.cursor()

    def commit(self):
        self.c

    def disconnect(self):
        self.cursor.close()

    def deleteFromTo(self, dateFrom, dateTo):
        """
        Delete all entries in the table from a date to another.
        Use the sqlite "created_at" attribute
        @param dateFrom: starting date, in sqlite format
        @param dateTo:  stoping date, sqlite format
        @return: the number of affected lines (deleted)
        """
        self.connect()
        res = self.cursor.execute("DELETE FROM "+self.tableName+" WHERE created_at >= '"+dateFrom+"' AND created_at <= '"+dateTo+"'").rowcount
        self.connection.commit()
        self.disconnect()
        return res


    def __del__(self):
       if(self.connection != None):
           self.disconnect()
