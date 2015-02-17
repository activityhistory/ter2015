import datetime

__author__ = 'maxime'

SCS_FORMAT = "%y%m%d-%H%M%S%f"
DB_FORMAT = "%Y-%m-%d %H:%M:%S.%f"


def SCStoDB(scs):
    scs = scs.split("_")[0] #remove the numbers after the first '_'
    return datetime.datetime.strptime(scs, SCS_FORMAT).strftime(DB_FORMAT)

def DBtoSCS(db):
    r = datetime.datetime.strptime(db, DB_FORMAT).strftime(SCS_FORMAT)
    r += "_000_000" #to have a good format to sort/compare
    return r

#made for SCS_FORMAT.
def addASecondAndTrucate(scsName):
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
    scs = scs.split(".")[0] # remove the ext
    scs = scs.split("_")[0] # remove after the _
    return datetime.datetime.strptime(scs, SCS_FORMAT)

