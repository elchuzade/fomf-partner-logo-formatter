# Logo Formatter - Flask Web App

A professional web application that formats logos with consistent sizing and padding. Built with Flask for robust performance and beautiful UI.

## Features

- **Modern Web Interface** - Beautiful, responsive design with drag & drop
- **Multi-format Support** - PNG, JPG, JPEG, and SVG files
- **Professional Processing** - Logos resized to fit within 260×180 pixels
- **Perfect Centering** - Logos centered on 300×220 canvas with padding
- **Quality Enhancement** - Sharpening and transparency removal
- **Instant Download** - Processed logos available immediately

## Local Development

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask app:**

   ```bash
   python app_flask.py
   ```

3. **Open your browser** and go to `http://localhost:5002`

## Deployment Options

### Option 1: Render (Recommended - Free)

1. Push your code to GitHub
2. Go to [render.com](https://render.com)
3. Create a new Web Service
4. Connect your GitHub repository
5. Set build command: `pip install -r requirements.txt`
6. Set start command: `python app_flask.py`
7. Deploy automatically

### Option 2: Railway

1. Push to GitHub
2. Go to [railway.app](https://railway.app)
3. Connect repository
4. Auto-deploys on push

### Option 3: Heroku

1. Install Heroku CLI
2. Create app: `heroku create your-app-name`
3. Deploy: `git push heroku main`

## File Structure

```
logo-formatter/
├── app_flask.py          # Flask application
├── logo_formatter.py     # Core logo processing logic
├── templates/
│   └── index.html        # Professional HTML template
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment configuration
├── runtime.txt           # Python version
└── README.md             # This file
```

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Image Processing**: Pillow, svglib
- **Styling**: Custom CSS with gradients and animations
- **Deployment**: Render, Railway, or Heroku

## Usage

1. **Upload**: Drag & drop or click to browse for logo files
2. **Process**: Automatic formatting with progress indicator
3. **Preview**: Side-by-side comparison of original vs. formatted
4. **Download**: Get your professionally formatted logo

## Benefits of Flask over Streamlit

✅ **Professional UI** - Custom HTML/CSS design  
✅ **Better Performance** - No Python overhead for UI  
✅ **Full Control** - Complete styling and layout control  
✅ **Scalability** - Handle more users efficiently  
✅ **Mobile Responsive** - Perfect on all devices  
✅ **Custom Features** - Drag & drop, animations, etc.

## Support

For issues or questions, check the error logs or contact support.
