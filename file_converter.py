import pytesseract
from pdf2image import convert_from_path
import poppler
import os

pytesseract.pytesseract.tesseract_cmd = "tesseract-ocr/tesseract.exe"

pdf = "uploads/test.pdf"

def pdf_to_img():
    pages = convert_from_path(pdf, 350, output_folder = "uploads", fmt = "jpg")
    return pages
"""
def save_img(pages):
    i = 1
    for page in pages:
        image_name = "Page " + str(i) + ".jpg"
        page.save(image_name, "JPEG")
        i = i + 1

# img to pdf_ocr
pdf = pytesseract.image_to_pdf_or_hocr("uploads/test.png", extension='pdf')
with open("results/ocr.pdf", "w+b") as f:
    f.write(pdf) # pdf type is bytes by default

def img_to_pdf(pdf):
    with open(pdf) as f:
        f.write(pdf)"""