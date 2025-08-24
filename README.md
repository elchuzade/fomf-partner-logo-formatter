# Logo Formatter Web App

A web application that formats logos with consistent sizing and padding. Upload your logo and get a professionally formatted version with a white background, centered on a 300x220 canvas.

## Features

- Supports PNG, JPG, JPEG, and SVG files
- Automatically resizes logos to fit within 260x180 pixels (maintaining aspect ratio)
- Centers logos on a 300x220 canvas with white background
- Removes transparency and applies sharpening
- Download processed logos as PNG files

## Local Development

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**

   ```bash
   streamlit run app.py
   ```

3. **Open your browser** and go to `http://localhost:8501`

## Deployment Options

### Option 1: Streamlit Cloud (Easiest)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy automatically

### Option 2: Heroku

1. Create a `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```
2. Deploy to Heroku

### Option 3: Docker

1. Build and run with Docker
2. Deploy to any cloud platform

## Usage

1. Upload your logo file
2. Wait for processing
3. Download the formatted logo
4. The processed logo will have consistent dimensions and padding

## File Structure

```
logo-formatter/
├── app.py              # Streamlit web app
├── logo_formatter.py   # Core logo processing logic
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── processed_logos/   # Output directory
```
