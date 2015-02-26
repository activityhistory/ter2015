import datetime

__author__ = 'maxime'

SCS_FORMAT = "%y%m%d-%H%M%S%f"
DB_FORMAT = "%Y-%m-%d %H:%M:%S.%f"


def SCStoDB(scs):
    """
    Parse screenshot format date to database (sqlite) format date
    @param scs: the name of teh screenshot (including the date) with or without the ".jpg"
    @return: the date on sqlite format
    """

    scs = scs.split("_")[0] #remove the numbers after the first '_'
    return datetime.datetime.strptime(scs, SCS_FORMAT).strftime(DB_FORMAT)

def DBtoSCS(db):
    """
    Parse the databse format date in screenshot format date
    @param db: the date in database format
    @return: the date in screenshot format date
    """
    r = datetime.datetime.strptime(db, DB_FORMAT).strftime(SCS_FORMAT)
    r += "_000_000" #to have a good format to sort/compare
    return r


def addASecondAndTrucate(scsName):
    """
    Add a second to a date, in Screenshot format
    @param scsName: the date in screenshot format
    @return: the date in screenshot format + 1 second, without names after "_", replaced by _000_000
    """
    scsName = scsName.split(".")[0] # remove the ext
    scsName = scsName.split("_")[0] # remove after the _
    date = datetime.datetime.strptime(scsName, SCS_FORMAT)
    date += datetime.timedelta(seconds=1)
    date = date.replace(microsecond=0)
    date = date.strftime(SCS_FORMAT)
    date +=  "_000_000"
    date += ".jpg"
    return date


def getDateBySCS(scs):
    """
    Return a Date object, made with a screenshot format date
    @param scs: screenshot format date
    @return: Date object
    """
    scs = scs.split(".")[0] # remove the ext
    scs = scs.split("_")[0] # remove after the _
    return datetime.datetime.strptime(scs, SCS_FORMAT)

