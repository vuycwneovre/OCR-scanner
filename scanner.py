import pytesseract
from PIL import Image 


pytesseract.pytesseract.tesseract_cmd = '<C:/Archivos de programa/Tesseract-OCR/tesseract.exe>'

filename = 'a.png'

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text


print(ocr_core(filename))