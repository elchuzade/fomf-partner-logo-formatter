from PIL import Image
import os
import tempfile
import shutil

# Import your existing process_logo function
from logo_formatter import process_logo

# Custom CSS for styling
st.set_page_config(
    page_title="Logo Formatter",
    page_icon="🎨",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: white;
    }
    .stApp {
        background-color: white;
    }
    .stTitle {
        color: #1f1f1f;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
    }
    .upload-section {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        border: 2px dashed #dee2e6;
        text-align: center;
        margin: 2rem 0;
    }
    .result-section {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .download-btn {
        background-color: #007bff;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        text-decoration: none;
        display: inline-block;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Header with company logo
# Company logo - centered across entire page
st.markdown("""
<div style="display: flex; justify-content: center; align-items: center; margin-bottom: 1rem;">
    <img src="https://storage.googleapis.com/bk-public-prod/public/static/logo/logo-fomf.svg" width="120" style="max-width: 120px;">
</div>
""", unsafe_allow_html=True)

st.markdown('<h1 class="stTitle">Logo Formatter</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #6c757d; font-size: 1.1rem;">Professional logo formatting with consistent sizing and padding</p>', unsafe_allow_html=True)

# Main content
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload a logo file (PNG, JPG, JPEG, SVG)", type=['png', 'jpg', 'jpeg', 'svg'])
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_input_path = tmp_file.name

    # Prepare output path
    temp_output_path = temp_input_path + "_processed.png"

    # Process the logo
    with st.spinner("Processing your logo..."):
        process_logo(temp_input_path, temp_output_path)

    # Results section
    st.markdown('<div class="result-section">', unsafe_allow_html=True)
    
    # Create two columns for side-by-side comparison
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📤 Original Image")
        # Handle SVG files differently for display
        if uploaded_file.name.lower().endswith('.svg'):
            # For SVG files, convert to PNG for preview
            try:
                # Create a temporary PNG for preview
                preview_path = temp_input_path + "_preview.png"
                from logo_formatter import convert_svg_to_png
                convert_svg_to_png(temp_input_path, preview_path, max_width=480, max_height=320)
                preview_image = Image.open(preview_path)
                # Use container for border effect
                with st.container():
                    st.markdown('<div style="border: 2px solid #dee2e6; padding: 10px; border-radius: 8px; background-color: #f8f9fa;">', unsafe_allow_html=True)
                    st.image(preview_image, width=480)
                    st.markdown('</div>', unsafe_allow_html=True)
                st.markdown(f"**File:** {uploaded_file.name}")
                # Clean up preview
                os.remove(preview_path)
            except Exception as e:
                st.info("📁 SVG file uploaded - will be processed and formatted")
                st.markdown(f"**File:** {uploaded_file.name}")
        else:
            # Reset file pointer and display original for raster images
            uploaded_file.seek(0)
            # Use container for border effect
            with st.container():
                st.markdown('<div style="border: 2px solid #dee2e6; padding: 10px; border-radius: 8px; background-color: #f8f9fa;">', unsafe_allow_html=True)
                st.image(uploaded_file, width=480)
                st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.subheader("✨ Processed Image")
        processed_image = Image.open(temp_output_path)
        # Use container for border effect
        with st.container():
            st.markdown('<div style="border: 2px solid #dee2e6; padding: 10px; border-radius: 8px; background-color: #f8f9fa;">', unsafe_allow_html=True)
            st.image(processed_image, width=300)
            st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Download section
    st.markdown('<div class="result-section">', unsafe_allow_html=True)
    st.subheader("💾 Download Processed Logo")
    
    with open(temp_output_path, "rb") as file:
        btn = st.download_button(
            label="📥 Download Processed Logo",
            data=file,
            file_name="processed_logo.png",
            mime="image/png",
            use_container_width=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Clean up temp files
    os.remove(temp_input_path)
    os.remove(temp_output_path)

else:
    # Show instructions when no file is uploaded
    st.markdown("""
    <div style="text-align: center; padding: 3rem; color: #6c757d;">
        <h3>How to use:</h3>
        <ol style="text-align: left; display: inline-block;">
            <li>Upload your logo file (PNG, JPG, JPEG, or SVG)</li>
            <li>Wait for processing to complete</li>
            <li>Download your formatted logo</li>
        </ol>
        <br>
        <p><strong>Your logo will be:</strong></p>
        <ul style="text-align: left; display: inline-block;">
            <li>Resized to fit within 260×180 pixels</li>
            <li>Centered on a 300×220 white canvas</li>
            <li>Enhanced with sharpening</li>
            <li>Saved as a high-quality PNG</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)