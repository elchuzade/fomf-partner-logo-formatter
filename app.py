import streamlit as st
from PIL import Image
import os
import tempfile
import shutil

# Import your existing process_logo function
from logo_formatter import process_logo

st.title("Logo Formatter")

uploaded_file = st.file_uploader("Upload a logo file (PNG, JPG, JPEG)", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_input_path = tmp_file.name

    # Prepare output path
    temp_output_path = temp_input_path + "_processed.png"

    # Process the logo
    process_logo(temp_input_path, temp_output_path)

    # Show original image
    st.subheader("Original Image")
    st.image(uploaded_file)

    # Show processed image
    st.subheader("Processed Image")
    processed_image = Image.open(temp_output_path)
    st.image(processed_image)

    # Provide download button for processed image
    with open(temp_output_path, "rb") as file:
        btn = st.download_button(
            label="Download Processed Logo",
            data=file,
            file_name="processed_logo.png",
            mime="image/png"
        )

    # Clean up temp files
    os.remove(temp_input_path)
    os.remove(temp_output_path)