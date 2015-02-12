__author__ = 'maxime'
import pytesseract
import Image

def OCR_SCS(SCSPath):
    img = Image.open(SCSPath)
    return pytesseract.image_to_string(img)
