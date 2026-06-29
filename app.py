from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
import subprocess
import os
import tempfile
from pathlib import Path

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max file size
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

ALLOWED_EXTENSIONS = {
    # Documents
    'pdf', 'docx', 'doc', 'pptx', 'ppt', 'xlsx', 'xls', 'csv', 'txt',
    # Images
    'png', 'jpg', 'jpeg', 'gif', 'svg', 'webp', 'bmp', 'tiff',
    # Web
    'html', 'htm', 'xml', 'json',
    # Media
    'mp3', 'mp4', 'webm', 'mov', 'avi', 'wav'
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        # Check if file is in request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if not allowed_file(file.filename):
            return jsonify({'error': f'File type not allowed. Supported types: {", ".join(sorted(ALLOWED_EXTENSIONS))}'}), 400

        # Save uploaded file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            # Run markitdown
            result = subprocess.run(
                ['markitdown', filepath],
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode != 0:
                return jsonify({'error': f'Conversion failed: {result.stderr}'}), 400

            markdown_content = result.stdout

            return jsonify({
                'success': True,
                'markdown': markdown_content,
                'filename': filename.rsplit('.', 1)[0] + '.md'
            })

        finally:
            # Clean up uploaded file
            if os.path.exists(filepath):
                os.remove(filepath)

    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Conversion timeout - file too large'}), 400
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/download', methods=['POST'])
def download():
    try:
        data = request.json
        markdown_content = data.get('markdown', '')
        filename = data.get('filename', 'converted.md')

        # Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(markdown_content)
            temp_path = f.name

        return send_file(
            temp_path,
            as_attachment=True,
            download_name=filename,
            mimetype='text/markdown'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
