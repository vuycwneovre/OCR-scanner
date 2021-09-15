from pdf2image import convert_from_path
import pytesseract
# import poppler, error importing library, tried environmental variables->paths

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"


"""pdf = 'C:/Users/admin/Documents/Python-Scripts/OCR-scanner/uploads/test.pdf'
pages = convert_from_path(pdf, 350)


i = 1 
for page in pages:
    image_name = "Page " + str(i) + ".jpg"
    page.save(image_name, "JPEG")
    i = i + 1"""


# Get a searchable PDF
pdf = pytesseract.image_to_pdf_or_hocr('C:/Users/VDI/Documents/GitHub/OCR-scanner/uploads/test.png', extension='pdf')
with open('C:/Users/VDI/Documents/GitHub/OCR-scanner/uploads/test1.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default