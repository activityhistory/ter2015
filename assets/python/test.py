__author__ = 'maxime'
import imageSetClass
import FilterByKeywordsClass
import sys
import json
import db_PrivacyKeywordsClass

#Path to the screenshots folder
SCS = "assets/images/screens/"
#Path to the OCRed screenshots ; txt
TXT = "assets/OCRed/"
#DB : path + name + ext
DB = "selfspy.sqlite"

db = db_PrivacyKeywordsClass.db_PrivacyKeywords(DB)
keywords = db.getAll()


#only to test !
#imgset = imageSetClass.imageSet("150129-190322843896_173_674.jpg", "150129-190444213350_155_693.jpg", SCS)


imgset = imageSetClass.imageSet(sys.argv[1], sys.argv[2], SCS)

fbk = FilterByKeywordsClass.FindByKeywords(SCS, TXT, keywords)
print  json.dumps(fbk.FilterByKeyWordsWithResultByImage(imgset))


