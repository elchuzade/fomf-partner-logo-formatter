from flask import Flask, render_template, request, send_file, jsonify
from logo_formatter import process_logo
import os
import tempfile
import uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'temp_uploads'
app.secret_key = 'your-secret-key-here'

# Create temp directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'svg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Please upload PNG, JPG, JPEG, or SVG files.'}), 400
    
    try:
        # Generate unique filename
        unique_id = str(uuid.uuid4())
        file_extension = os.path.splitext(file.filename)[1]
        temp_input_path = os.path.join(app.config['UPLOAD_FOLDER'], f"input_{unique_id}{file_extension}")
        temp_output_path = os.path.join(app.config['UPLOAD_FOLDER'], f"output_{unique_id}.png")
        
        # Save uploaded file
        file.save(temp_input_path)
        
        # Process the logo
        process_logo(temp_input_path, temp_output_path)
        
        # Check if output file was created
        if not os.path.exists(temp_output_path):
            return jsonify({'error': 'Failed to process logo'}), 500
        
        # Return the processed image
        return send_file(temp_output_path, mimetype='image/png', as_attachment=True, download_name='processed_logo.png')
        
    except Exception as e:
        return jsonify({'error': f'Error processing logo: {str(e)}'}), 500
    
    finally:
        # Clean up temp files
        try:
            if os.path.exists(temp_input_path):
                os.remove(temp_input_path)
            if os.path.exists(temp_output_path):
                os.remove(temp_output_path)
        except:
            pass

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5002)))
