__author__ = 'maxime'
import imageSetClass
import FilterByKeywordsClass
import sys
import json
import db_PrivacyKeywordsClass
import db_virtual_activeWindowClass

#Path to the screenshots folder
SCS = "assets/images/screens/"
#Path to the OCRed screenshots ; txt
TXT = "assets/OCRed/"
#DB : path + name + ext
DB = "selfspy.sqlite"


#to test :
#SCS = "scs/"
#TXT = "txt/"

#init the dbs
db_keywords = db_PrivacyKeywordsClass.db_PrivacyKeywords(DB)
db_focusedApp = db_virtual_activeWindowClass.db_virtual_activeWindow(DB)


#extract the keywords
keywords = db_keywords.getAll()


#only to test !
#imgset = imageSetClass.imageSet("150129-191418765697_994_99.jpg", "150129-191519379681_1026_834.jpg", SCS)


imgset = imageSetClass.imageSet(sys.argv[1], sys.argv[2], SCS)

#init the filter
fbk = FilterByKeywordsClass.FindByKeywords(SCS, TXT, keywords)
#filter and group by images differences
lst = fbk.FilterByKeywords(imgset)
#add the focused app to the list
db_focusedApp.setTheActiveAppInAllImagesSet(lst)

print json.dumps(lst, cls=imageSetClass.imageSetEncoder)

