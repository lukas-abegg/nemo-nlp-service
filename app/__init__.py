from flask import Flask, redirect, url_for
from flaskext.markdown import Markdown

app = Flask(__name__)
app.secret_key = "b'X\x97#\xad\xf1&\xa2\x95\x8c\xa0u-\x86\xe4\x8a\xe7'"
Markdown(app)

from app.ner_tagging import tagger
from app.summarization import summarizers
from app.similarity import similarity_calculation


@app.route('/')
def index():
    return redirect(url_for('ner_extractor'))
