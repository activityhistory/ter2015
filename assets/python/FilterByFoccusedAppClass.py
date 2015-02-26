__author__ = 'maxime'

import db_ProcessClass

import imageSetClass

class FilterByFoccusedApp:
    """
        Filter ImageSet or a List of ImageSet By foccused App
        Focused app should already provided in the image set (use db_locationClass)
    """



    notAllowedAppList = None

    def __init__(self, db):
        """
        Constructor
        @param db: the path and the nome of the deb where there is process table
        @return: None
        """
        #Here take back the app not alloweded
        self.notAllowedAppList = db_ProcessClass.db_Process(db).getNotAllowedAppList()


    def doFilterOnImgSetList(self, imgSetList):
        """
        Filter imageSetList by focussed app
        Focused app should already provided in the image set (use db_locationClass)
        @param imgSetList: an array of ImageSet instances, foccused ap informed in each imageSet
        @return: None
        """
        for imgset in imgSetList:
            self.doFilterOnOneImgSet(imgset)

    def doFilterOnOneImgSet(self, imgset):
        """
        Filter ine imageSe by focussed app
        Focused app should already provided in the image set (use db_locationClass)
        @param imgSetList: an array of ImageSet instances, foccused ap informed in each imageSet
        @return: None
        """
        for app in self.notAllowedAppList :
            if(app == imgset.focusedApp):
                imgset.setUnAcceptable()
                imgset.addFiltredBy("Focused application")
                return


# to test
# imgset = imageSetClass.imageSet("150216-110328445757_795_724.jpg", "150216-135201526688_402_637.jpg", "scs/")
# test = FilterByFoccusedApp("../../selfspy.sqlite")
# print test.notAllowedAppList
# test.doFilterOnOneImgSet(imgset)
# print imgset.location

# print test.haversine(4.830587, 45.776692, 4.830587000000037, 45.776692 ) < 400