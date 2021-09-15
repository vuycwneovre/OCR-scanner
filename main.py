from typing import Text
import pytesseract
from PIL import Image 
import numpy as np
import cv2
import preprocessing 

pytesseract.pytesseract.tesseract_cmd = "tesseract-ocr/tesseract.exe"

img = Image.open("uploads/test.png")


# print results in console
def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text
print(ocr_core(img))


# write results in a .txt
f = open ("results/results.txt", "w")
f.write(pytesseract.image_to_string(img))
f.close()
