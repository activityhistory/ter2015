__author__ = 'maxime'

import db_PrivacyKeywordsClass

db = db_PrivacyKeywordsClass.db_PrivacyKeywords("selfspy.sqlite")
for kw in  db.getAll():
    print kw