import imageSetClass

__author__ = 'maxime'

import db_Privacy_LocationClass
import db_LocationClass
import DateParser
from math import radians, cos, sin, asin, sqrt

class FilterByLocation:

    MINDIST = 400 #meters
    dbLocation = None
    userLocations = None
    dbUserLocation = None

    def __init__(self, db):
        self.dbLocation = db_LocationClass.db_Location(db)
        self.dbUserLocation = db_Privacy_LocationClass.db_Privacy_Location(db)
        self.userLocations = self.dbUserLocation.getUserLocationList()

    def setOneImageSetLocation(self, imgset):
        (lon, lat) = self.dbLocation.getLastLocationAtTime(DateParser.SCStoDB(imgset.stop))
        imgset.setLocation(lon, lat)

    def setLocationListOfImageSet(self, imgsetList):
        for imgset in imgsetList:
            self.setOneImageSetLocation(imgset)

    def setAndFilterImageSetList(self, imgSetList):
        self.setLocationListOfImageSet(imgSetList)
        self.FilterImageSetList(imgSetList)

    def FilterImageSetList(self, imgSetList):
        for imgSet in imgSetList:
            self.FilterOneImageSet(imgSet)

    def FilterOneImageSet(self, imgset):
        (imgSetLat, imgSetLon) = imgset.location
        for (lon, lat) in self.userLocations :
            if(self.haversine(lon, lat, imgSetLon, imgSetLat) < self.MINDIST):
                imgset.locationName = self.dbUserLocation.getLocationUserName(lat, lon)
                if self.dbUserLocation.isAPrivateLocation(lat, lon):
                    imgset.setUnAcceptable()
                    imgset.addFiltredBy("Location")
        if imgset.locationName is None :
            imgset.locationName = "Unknow ("+str(lat)+", "+str(lon)+")"
            imgset.setUnAcceptable()
            imgset.addFiltredBy("Location")

    def haversine(self, lon1, lat1, lon2, lat2):

        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        return (c * r)*1000

# imgset = imageSetClass.imageSet("150216-110235592918_1057_514.jpg", "150216-110310916869_1057_262.jpg", "scs/")
# test = FilterByLocation("../../selfspy.sqlite")
# test.setOneImageSetLocation(imgset)
# print imgset.location
# test.FilterOneImageSet(imgset)