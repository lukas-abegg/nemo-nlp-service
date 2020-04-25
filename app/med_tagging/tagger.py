from app import app

from flask import render_template, request
from spacy import displacy

from app.spacy.spacy_models import MODELS

import time


@app.route('/med_tagger')
def med_tagger():
    return render_template('med_tagger.html')


@app.route('/med_tagger_extracted', methods=["GET", "POST"])
def med_tagger_extracted():
    start = time.time()
    if request.method == 'POST':
        raw_text = request.form['rawtext']

        # en_core_sci_sm
        start_core = time.time()
        nlp_core = MODELS['en_core_sci_sm']
        docx_core = nlp_core(raw_text)
        html_core = displacy.render(docx_core, style="ent")
        html_core = html_core.replace("\n\n", "\n")
        end_core = time.time()
        tagging_gen_time_core = end_core - start_core

        # en_ner_bc5cdr_md
        start_spacy = time.time()
        nlp_spacy = MODELS['en_ner_bc5cdr_md']
        docx_spacy = nlp_spacy(raw_text)
        html_spacy = displacy.render(docx_spacy, style="ent")
        html_spacy = html_spacy.replace("\n\n", "\n")
        end_spacy = time.time()
        tagging_gen_time_spacy = end_spacy - start_spacy

        end = time.time()
        final_time = end - start
    return render_template('med_tagger_extracted.html',
                           rawtext=raw_text,
                           result_core=html_core,
                           tagging_gen_time_core=tagging_gen_time_core,
                           result_spacy=html_spacy,
                           tagging_gen_time_spacy=tagging_gen_time_spacy,
                           final_time=final_time
                           )
