
import db_BaseClass
import os

class db_Windowevent(db_BaseClass.db_Base):

    def __init__(self, dbname):
        db_BaseClass.db_Base.__init__(self, dbname)
        self.tableName = "windowevent"