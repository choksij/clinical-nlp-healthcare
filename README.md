# Clinical Natural Language Processing

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Install Dependencies](#install-dependencies)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Acknowledgments](#acknowledgments)

## Introduction
The Medical Document and Image Analysis project is a Flask-based web application designed to process and analyze medical documents and images. The application extracts text from medical images using Optical Character Recognition (OCR), analyzes the text for key medical entities and summaries using Natural Language Processing (NLP), and classifies medical images (e.g., X-rays, MRIs) using a pre-trained deep learning model.

## Features
- **OCR Processing**: Extracts text from medical documents (images) using Tesseract OCR.
- **NLP Analysis**: Identifies named entities (e.g., diseases, medications) and generates a summary of the extracted text using spaCy and Hugging Face's transformers.
- **Image Classification**: Classifies medical images using a pre-trained ResNet model.
- **User-Friendly Interface**: Simple web interface for uploading and analyzing medical documents and images.
- **Error Handling**: Robust error handling with informative logging.

## Project Structure
├── app.py # Main Flask application

├── ocr.py # OCR processing module

├── nlp.py # NLP processing module

├── vision.py # Image classification module

├── utils.py # Utility functions

├── templates/

│ └── index.html # HTML template for the web interface

├── static/

│ └── uploads/ # Directory for uploaded files

├── setup.py # Setup script for the project

├── requirements.txt # Project dependencies

└── README.md # Project README file


## Installation

### Prerequisites
- Python 3.8 or higher
- Tesseract OCR (Ensure it's installed and accessible via the command line)

## Install Dependencies

pip install -r requirements.txt



## Usage
- **Upload a Medical Document or Image**: On the home page, you can upload either a medical document (as an image) or a medical image (like an X-ray or MRI).
- **View Analysis Results**: After uploading, the OCR text, identified entities, summary, and image classification result will be displayed.

## Technologies Used
- **Flask**: Web framework for Python.
- **Tesseract OCR**: Optical Character Recognition engine.
- **spaCy**: NLP library for entity recognition.
- **Transformers**: Hugging Face library for text summarization.
- **PyTorch & torchvision**: Libraries for deep learning and image processing.
- **Bootstrap**: Frontend framework for responsive design.
  
## Acknowledgments

- **spaCy**: Industrial-strength Natural Language Processing in Python.
- **Hugging Face**: Transformers for State-of-the-Art Natural Language Processing.
- **Tesseract OCR**: Open-source OCR engine.
- **PyTorch**: Deep learning framework.

### Clone the Repository
```bash
git clone https://github.com/choksij/clinical-nlp-healthcare.git
cd medical_analysis
