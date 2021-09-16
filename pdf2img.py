from pdf2image import convert_from_path
import poppler
import os

pdf = "uploads/test.pdf"
pages = convert_from_path(pdf, 350)

i = 1 
for page in pages:
    image_name = "Page " + str(i) + ".jpg"
    path = "/uploads"
    page.save(image_name, "JPEG")
    i = i + 1