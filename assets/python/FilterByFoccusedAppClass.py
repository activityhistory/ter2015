__author__ = 'maxime'



class FilterByFoccusedApp:

    notAllowedAppList = None

    def __init__(self):
        #Here take back the app not allowededdeded
        self.notAllowedAppList = ["Firefox", "Pages", "Postbox"]


    def doFilterOnImgSetList(self, imgSetList):
        for imgset in imgSetList:
            self.doFilterOnOneImgSet(imgset)

    def doFilterOnOneImgSet(self, imgset):
        for app in self.notAllowedAppList :
            if(app == imgset.focusedApp):
                imgset.setUnAcceptable()
                return
