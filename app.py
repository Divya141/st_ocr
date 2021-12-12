import streamlit as st
import cv2
import pytesseract
from PIL import Image #python imaging libraries to open images
import numpy as np
pytesseract.pytesseract.tesseract_cmd = "/app/.apt/usr/bin/tesseract"
st.set_option('deprecation.showfileUploaderEncoding',False)
st.title("Optical character recognition")
st.text("Upload the image")
uploaded_file = st.sidebar.file_uploader("Chose an image:", type=["jpg","png","jpeg"])
if uploaded_file is not None:
  img=Image.open(uploaded_file)
  st.image(img, caption='Uploaded Image',use_column_width=True)
  st.write("")
  if st.button("PREDICT"):
    st.write("Result:")
    info = pytesseract.image_to_string(img)
    st.title(info)
