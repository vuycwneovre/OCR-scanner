# OCR scanner using Tesseract
 
 This scanner uses Tesseract to obtain text from a picture.  
 
 It provides also:
   - IMG to PDF
   - OCR for PDF
   - PDF to IMG

 To use Poppler I had to follow this guide: https://towardsdatascience.com/poppler-on-windows-179af0e50150. It did not work before that, even adding the path to environmental variables.

 To install Tesseract I used this repository at UB- Mannheim https://github.com/UB-Mannheim/tesseract/wiki
 
 To display an interface Streamlit(https://streamlit.io/) is used.

 It is designed to work when tesseract-ocr folder is installed in the root of the project. 

# In the future

 - Preprocessing for the IMG's with Open CV and some of the following libraries https://tesseract-ocr.github.io/tessdoc/ImproveQualit, like https://github.com/leha-bot/PRLib
 - Keep improving Streamlit front: select language, copy to clipboard, etc.
 - Maybe FDroid App?

# Credits
   - https://towardsdatascience.com/implementing-optical-character-recognition-ocr-using-pytesseract-5f42cf62ddcc
   - https://nanonets.com/blog/ocr-with-tesseract/#introduction
   - https://github.com/Rokon-Uz-Zaman/CamScanner-In-Python_OpenCV
   - https://towardsdatascience.com/extracting-text-from-scanned-pdf-using-pytesseract-open-cv-cd670ee38052
   - https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/
   - https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py
