import streamlit as st
import numpy as np
import pandas as pd
import main
from PIL import Image
import pytesseract

st.header('OCR-scanner, in Python')
st.text('using Tesseract and Open CV')

uploaded_file = st.file_uploader('Select your file', type = ['jpg','png','jpeg','JPG'])

def load_image(uploaded_file):
	img = Image.open(uploaded_file)
	return img

if uploaded_file is not None:
    st.image(load_image(uploaded_file))