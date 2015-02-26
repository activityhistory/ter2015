import cv2
import imageSetClass
import os

__author__ = 'maxime'

class imagesGrouper:
    """
    Group all images on one image set to make smaller imager set, of dfferetes activitties
    Using the image Color histogram distage to separe each slots
    """

    def __init__(self, scsRelativePath, MIN_DIST=0.995):
        self.scsRelativePath = scsRelativePath
        self.MIN_DIST = MIN_DIST

    def group(self, imgset):


        #The list of all image, sorted
        lstImg = imgset.getSortedImagesList()

        lstImgSet = []
        currentimageSetStart = lstImg[0]

        for i in range(len(lstImg)-1) :
            dist = self.compare(lstImg[i], lstImg[i+1])
            if dist < self.MIN_DIST:
                lstImgSet.append(imageSetClass.imageSet(currentimageSetStart, lstImg[i], imgset.relativePath))
                currentimageSetStart = lstImg[i+1]
        #add the last one
        lstImgSet.append(imageSetClass.imageSet(currentimageSetStart, lstImg[len(lstImg)-1], imgset.relativePath))

        return lstImgSet

    def compare(self, nameImage1 , nameImage2) :
        """
        Compare two images
        @param nameImage1:
        @param nameImage2:
        @return:
        """

        pathImage1 = os.path.join(self.scsRelativePath, nameImage1)
        pathImage2 = os.path.join(self.scsRelativePath, nameImage2)

        image1 = cv2.imread(pathImage1)
        image2 = cv2.imread(pathImage2)

        image1 = cv2.cvtColor(image1, cv2.cv.CV_BGR2HSV)
        image2 = cv2.cvtColor(image2, cv2.cv.CV_BGR2HSV)


        hist1 = cv2.calcHist([image1],[0],None,[256],[0,256])
        hist2 = cv2.calcHist([image2],[0],None,[256],[0,256])

        hist1 = cv2.normalize(hist1)
        hist2 = cv2.normalize(hist2)

        return cv2.compareHist(hist1, hist2, cv2.cv.CV_COMP_CORREL)

