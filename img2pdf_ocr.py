import pytesseract


pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

pdf = pytesseract.image_to_pdf_or_hocr('C:/Users/VDI/Documents/GitHub/OCR-scanner/uploads/test.png', extension='pdf')
with open('C:/Users/VDI/Documents/GitHub/OCR-scanner/results/ocr.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default