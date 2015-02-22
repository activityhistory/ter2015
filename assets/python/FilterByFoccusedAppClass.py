__author__ = 'maxime'

import db_ProcessClass

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
