from pdf2image import convert_from_path
import poppler
import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "tesseract-ocr/tesseract.exe"


#img2pdf_ocr
pdf = pytesseract.image_to_pdf_or_hocr("uploads/test.png", extension='pdf')
with open("results/ocr.pdf", "w+b") as f:
    f.write(pdf) # pdf type is bytes by default


#pdf2img
pdf = "uploads/test.pdf"
pages = convert_from_path(pdf, 350)

i = 1 
for page in pages:
    image_name = "Page " + str(i) + ".jpg"
    path = "/uploads"
    page.save(image_name, "JPEG")
    i = i + 1