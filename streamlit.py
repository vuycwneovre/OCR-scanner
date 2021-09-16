import streamlit as st
from PIL import Image
from main import ocr_core

st.header('OCR-scanner, in Python')
st.text('using Tesseract and Open CV')

uploaded_file = st.file_uploader('Select your file', type = ['jpg','png','jpeg','JPG','PDF'])

def load_image(uploaded_file):
	img = Image.open(uploaded_file)
	return img

if uploaded_file is not None:
    st.image(load_image(uploaded_file)) and st.write(ocr_core(Image.open(uploaded_file)))