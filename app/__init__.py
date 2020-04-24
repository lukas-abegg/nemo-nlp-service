from flask import Flask, redirect, url_for
from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)

from app.ner_tagging import tagger
from app.summarization import summarizers


@app.route('/')
def index():
    return redirect(url_for('ner_extractor'))
