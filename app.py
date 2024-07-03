import streamlit as st
from PIL import Image
import io
from color_palette import get_palette

st.title("Dominant Color Palette Generator")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Generating palette...")

    palette = get_palette(image, 5)

    st.write("Dominant Colors:")

    cols = st.columns(5)
    for i, color in enumerate(palette):
        with cols[i]:
            st.color_picker("", f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}', disabled=True, label_visibility='collapsed')
