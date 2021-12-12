%%writefile app.py
import streamlit as st
import cv2
import pytesseract
from PIL import Image #python imaging libraries to open images
import numpy as np
st.title("Optical character recognition")
st.text("Upload the image")
uploaded_file=st.sidebar.fileuploader("Chose an image:",type=["jpg","png","jpeg"])
if uploaded_file is not None:
  img=Image.open(uploaded_file)
  st.write("")
  if st.button("PREDICT"):
    st.write("Result:")
    info=pytesseract.image_to_string(img)
    st.title(info)
