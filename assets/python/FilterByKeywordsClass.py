__author__ = 'maxime'

import imageSetClass
import imagesGrouperClass
import OCR
import FindOrOCRClass
import FindOrOCRClass


class FindByKeywords :

    def __init__(self, screenshotsRelativePath, textsRelativePath, keywords):
        self.findOrOCR = FindOrOCRClass.FindOrOCR(screenshotsRelativePath, textsRelativePath)
        self.grouper = imagesGrouperClass.imagesGrouper(screenshotsRelativePath)
        self.keywords = keywords

    def FilterByKeyWordsWithResultByImage(self, imgset):
        res = self.FilterByKeywords(imgset)
        tabResByImage = []
        for lot in res:
            for i in range(len(lot)):
                if(lot.acceptable == True):
                    tabResByImage.append(0)
                else:
                    tabResByImage.append(1)

        return tabResByImage



    def FilterByKeywords(self, imgset):
        listGroup = self.grouper.group(imgset)
        for imgGroup in listGroup:
            #Here, we set the OCRed Text in the imgset
            OCRedTxt = self.findOrOCR.getText(imgGroup.stop)
            imgGroup.setOCRedText(OCRedTxt)

            if(self.SearchKeywords(OCRedTxt)): #if one keyword or more was find
                imgGroup.setUnAcceptable()
        return listGroup



    def SearchKeywords(self, string):
        string = string.decode('utf-8')
        for kw in self.keywords:
            kw = kw.decode('utf-8')
            if(string.find(kw) != -1):
                return True; # Find
        return False;