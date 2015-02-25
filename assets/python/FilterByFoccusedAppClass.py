__author__ = 'maxime'

import db_ProcessClass

import imageSetClass

class FilterByFoccusedApp:

    notAllowedAppList = None

    def __init__(self, db):
        #Here take back the app not allowededdeded
        self.notAllowedAppList = db_ProcessClass.db_Process(db).getNotAllowedAppList()


    def doFilterOnImgSetList(self, imgSetList):
        for imgset in imgSetList:
            self.doFilterOnOneImgSet(imgset)

    def doFilterOnOneImgSet(self, imgset):
        for app in self.notAllowedAppList :
            if(app == imgset.focusedApp):
                imgset.setUnAcceptable()
                imgset.addFiltredBy("Focused application")
                return



imgset = imageSetClass.imageSet("150216-110328445757_795_724.jpg", "150216-135201526688_402_637.jpg", "scs/")
test = FilterByFoccusedApp("../../selfspy.sqlite")
print test.notAllowedAppList
test.doFilterOnOneImgSet(imgset)
print imgset.location

# print test.haversine(4.830587, 45.776692, 4.830587000000037, 45.776692 ) < 400