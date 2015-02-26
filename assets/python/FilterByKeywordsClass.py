__author__ = 'maxime'

import imageSetClass
import imagesGrouperClass
import OCR
import FindOrOCRClass
import FindOrOCRClass


class FindByKeywords :
    """
    This class should be "FilterByKeywords" ...
    So...
    Filter image set by keywords entred by user...
    usage :
    f = FindByKeywords(Path_to_screenshots_folder, path_to_OCRed_text_files_folder, list_of_keywords_to_filterd_by)
    f.FilterByKeywords(imagesSetArray)
    """
    def __init__(self, screenshotsRelativePath, textsRelativePath, keywords):
        """
        Constructor
        @param screenshotsRelativePath:
        @param textsRelativePath:
        @param keywords:
        @return:
        """
        self.findOrOCR = FindOrOCRClass.FindOrOCR(screenshotsRelativePath, textsRelativePath)
        self.grouper = imagesGrouperClass.imagesGrouper(screenshotsRelativePath)
        self.keywords = keywords


    def FilterByKeyWordsWithResultByImage(self, imgset):
        """
        Depreciated
        Filter, and return a 0/1 array of each image of each imageSet
        @param imgset: ImageSet Instance
        @return: binary array
        """
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
        """
        #TODO : separe the grouper and the filter
        Firstly, groupe each image in the unique imageset argument , using imageGrouper
        Filter by keywords each imageSet in imageSetList
        @param imgset: One imageSet instance
        @return:imageSet instaces list, filterd by keywords
        """
        listGroup = self.grouper.group(imgset)
        for imgGroup in listGroup:
            #Here, we set the OCRed Text in the imgset
            OCRedTxt = self.findOrOCR.getText(imgGroup.stop)
            imgGroup.setOCRedText(OCRedTxt)

            if(self.SearchKeywords(OCRedTxt)): #if one keyword or more was find
                imgGroup.setUnAcceptable()
                imgGroup.addFiltredBy("Keyword or manual added application")
        return listGroup



    def SearchKeywords(self, string):
        """
        Looking for a keyword in a string
        return false at the first keyword finded
        #TODO : remove the case sensitive finder
        @param string: the text where you want to search if it contain any keyword
        @return: True if any keyword math, False else
        """
        string = string.decode('utf-8')
        for kw in self.keywords:
            kw = kw.decode('utf-8')
            if(string.find(kw) != -1):
                return True; # Find
        return False;