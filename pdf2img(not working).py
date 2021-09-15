from pdf2image import convert_from_path
# import poppler, error importing library, tried environmental variables->paths


pdf = 'C:/Users/admin/Documents/GitHub/OCR-scanner/uploads/test.pdf'
pages = convert_from_path(pdf, 350)


i = 1 
for page in pages:
    image_name = "Page " + str(i) + ".jpg"
    page.save(image_name, "JPEG")
    i = i + 1
