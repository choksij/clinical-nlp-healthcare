import spacy
from transformers import pipeline
import logging

logger = logging.getLogger(__name__)

nlp = spacy.load("en_core_web_sm")

def analyze_text(text):
    try:
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        summarizer = pipeline("summarization")
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        logger.info('NLP analysis successful')
        return entities, summary[0]['summary_text']
    except Exception as e:
        logger.error(f'Error during NLP analysis: {e}')
        raise
