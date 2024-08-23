import pytesseract
from PIL import Image
import logging

logger = logging.getLogger(__name__)

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def perform_ocr(image_path):
    try:
        image = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(image)
        logger.info('OCR extraction successful')
        return extracted_text
    except Exception as e:
        logger.error(f'Error during OCR extraction: {e}')
        raise
