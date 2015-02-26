__author__ = 'maxime'
import imageSetClass
import sys
import CleanerClass

"""
Script that clean all data between two dates
"""

#Path to the screenshots folder
SCS = "assets/images/screens/"
#Path to the OCRed screenshots ; txt
TXT = "assets/OCRed/"
#DB : path + name + ext
DB = "selfspy.sqlite"


#to test :
#SCS = "scs/"
#TXT = "txt/"


#only to test !
#imgset = imageSetClass.imageSet("150129-191418765697_994_99.jpg", "150129-191519379681_1026_834.jpg", SCS)


imgset = imageSetClass.imageSet(sys.argv[1], sys.argv[2], SCS)

print CleanerClass.Cleaner(imgset, SCS, TXT, DB).clean()
