__author__ = 'maxime'
import imageSetClass
import FilterByKeywordsClass
import sys
import json
import db_PrivacyKeywordsClass
import db_virtual_activeWindowClass
import demjson


#Path to the screenshots folder
SCS = "assets/images/screens/"
#Path to the OCRed screenshots ; txt
TXT = "assets/OCRed/"
#DB : path + name + ext
DB = "selfspy.sqlite"


#to test :
SCS = "scs/"
TXT = "txt/"

db = db_PrivacyKeywordsClass.db_PrivacyKeywords(DB)
keywords = db.getAll()


#only to test !
imgset = imageSetClass.imageSet("150129-191418765697_994_99.jpg", "150129-191528630390_656_63.jpg", SCS)


#imgset = imageSetClass.imageSet(sys.argv[1], sys.argv[2], SCS)

fbk = FilterByKeywordsClass.FindByKeywords(SCS, TXT, keywords)
lst = fbk.FilterByKeywords(imgset)
dbW = db_virtual_activeWindowClass.db_virtual_activeWindow("selfspy.sqlite")
dbW.setTheActiveAppInAllImagesSet(lst)

print json.dump(lst)

#for img in lst:
#    print img.to_JSON()