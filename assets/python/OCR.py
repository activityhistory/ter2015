__author__ = 'maxime'
import pytesseract
import Image



def OCR_SCS(SCSPath):
    """
    Do OCR of the imafe in SCSPath
    @param SCSPath: path and name (and ext) of the image to OCR
    @return: OCRed Text
    """
    img = Image.open(SCSPath)
    return pytesseract.image_to_string(img)
