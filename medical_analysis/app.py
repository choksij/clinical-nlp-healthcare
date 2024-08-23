from flask import Flask, render_template, request, redirect, url_for, flash
import os
import logging
from werkzeug.utils import secure_filename

from ocr import perform_ocr
from nlp import analyze_text
from vision import analyze_image
from utils import allowed_file, map_class_id_to_name

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'medical_analysis/static/uploads/'
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'document' in request.files and allowed_file(request.files['document'].filename):
            doc_file = request.files['document']
            filename = secure_filename(doc_file.filename)
            doc_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            doc_file.save(doc_path)

            try:
                document_text = perform_ocr(doc_path)
                entities, summary = analyze_text(document_text)
                logger.info(f'OCR and NLP processing successful for document {filename}')
                return render_template('index.html', ocr_text=document_text, entities=entities, summary=summary)
            except Exception as e:
                logger.error(f'Error during OCR/NLP processing: {e}')
                flash('An error occurred during document processing.')
                return redirect(url_for('index'))

        elif 'image' in request.files and allowed_file(request.files['image'].filename):
            img_file = request.files['image']
            filename = secure_filename(img_file.filename)
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img_file.save(img_path)

            try:
                image_analysis_result = analyze_image(img_path)
                class_name = map_class_id_to_name(image_analysis_result)
                logger.info(f'Image analysis successful for image {filename}')
                return render_template('index.html', image_result=class_name)
            except Exception as e:
                logger.error(f'Error during image analysis: {e}')
                flash('An error occurred during image processing.')
                return redirect(url_for('index'))

        else:
            flash('Invalid file type. Please upload an image file.')
            return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
