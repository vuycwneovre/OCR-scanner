from typing import Text
import pytesseract
from PIL import Image 


pytesseract.pytesseract.tesseract_cmd = r'<C:\Users\admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe>'

img = Image.open('C:/Users/admin/Documents/github-upload/camera_scanner/test2.png')

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    print(text)
    return text

print(ocr_core(img))

def main():
    print(ocr_core())
