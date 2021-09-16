import streamlit as st
import os
from PIL import Image
from main import ocr_core 
from file_converter import pdf_to_img

#displays img in streamlit front
def load_image(uploaded_file):
	img = Image.open(uploaded_file)
	return img
# gets files and saves them in uploads
def save_uploaded_file(uploaded_file):
     with open(os.path.join("uploads",uploaded_file.name),"wb") as f:
         f.write(uploaded_file.getbuffer())
     return st.success("Saved File:{} to uploads".format(uploaded_file.name))


st.header('OCR-scanner, in Python')
st.text('using Tesseract and Open CV')

uploaded_file = st.file_uploader('Select your file', type = ['jpg', 'JPG', 'png','jpeg','pdf','PDF'])

if uploaded_file is not None:
    save_uploaded_file(uploaded_file)

for file in os.listdir("uploads"):
	if file.lower().endswith(".pdf"):
		pdf_to_img(uploaded_file)
		st.write(ocr_core(Image.open(uploaded_file)))
	else:
		st.write(ocr_core(Image.open(uploaded_file)))