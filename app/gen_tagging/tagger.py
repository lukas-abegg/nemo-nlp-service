from app import app

from flask import render_template, request
from spacy import displacy

from app.spacy.spacy_models import MODELS

import time


@app.route('/gen_tagger')
def gen_tagger():
    return render_template('gen_tagger.html')


def render_entities_tagged(nlp, text: str):
    docx_core = nlp(text)
    html_core = displacy.render(docx_core, style="ent")
    return html_core.replace("\n\n", "\n")


@app.route('/gen_tagger_extracted', methods=["GET", "POST"])
def gen_tagger_extracted():
    start = time.time()
    if request.method == 'POST':
        raw_text = request.form['rawtext']
        lang = request.form['lang']

        # Spacy NER Tagger
        start_spacy = time.time()
        if lang == "de":
            lang_text = "German"
            nlp_spacy = MODELS['de_core_news_sm']
        else:
            lang_text = "English"
            nlp_spacy = MODELS['en_core_web_sm']
        html_spacy = render_entities_tagged(nlp_spacy, raw_text)
        end_spacy = time.time()
        tagging_gen_time_spacy = end_spacy - start_spacy

        end = time.time()
        final_time = end - start
    return render_template('gen_tagger_extracted.html',
                           rawtext=raw_text,
                           result_spacy=html_spacy,
                           tagging_gen_time_spacy=tagging_gen_time_spacy,
                           final_time=final_time,
                           lang=lang_text
                           )
