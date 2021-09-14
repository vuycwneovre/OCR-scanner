import pytesseract
from PIL import Image 
import numpy as np
import cv2
#import preprocessing

pytesseract.pytesseract.tesseract_cmd = "C:/Users/admin/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"

img = Image.open('C:/Users/admin/Documents/Python-Scripts/OCR-scanner/uploads/test.png')

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

print(ocr_core(img))



"""gray = get_grayscale(image)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray) """