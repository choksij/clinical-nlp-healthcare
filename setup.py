from setuptools import setup, find_packages

setup(
    name='medical_analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'pytesseract',
        'Pillow',
        'spacy',
        'torch',
        'transformers',
        'torchvision',
    ],
)
