from typing import Text
import pytesseract
from PIL import Image 
import numpy as np
import cv2
import preprocessing 

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

img = Image.open('C:/Users/VDI/Documents/GitHub/OCR-scanner/uploads/test.png')

#preprocessing
"""gray = preprocessing.get_grayscale(img)
thresh =  preprocessing.thresholding(gray)
opening =  preprocessing.opening(gray)
canny =  preprocessing.canny(gray)"""

# print results in console
def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text
print(ocr_core(img))

# write results in a .txt
f = open ("C:/Users/VDI/Documents/GitHub/OCR-scanner/results/results.txt", "w")
f.write(pytesseract.image_to_string(img))
f.close()
