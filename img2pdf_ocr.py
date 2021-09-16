import pytesseract

pytesseract.pytesseract.tesseract_cmd = "tesseract-ocr/tesseract.exe"

pdf = pytesseract.image_to_pdf_or_hocr("uploads/test.png", extension='pdf')
with open("results/ocr.pdf", "w+b") as f:
    f.write(pdf) # pdf type is bytes by default
