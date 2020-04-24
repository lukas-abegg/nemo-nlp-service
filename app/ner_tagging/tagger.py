from app import app

from flask import render_template, request
import spacy
from spacy import displacy

import time

print("Loading...")
MODELS = {
    "en_core_web_sm": spacy.load("en_core_web_sm"),
    "en_trf_bertbaseuncased_lg": spacy.load("en_trf_bertbaseuncased_lg")
}
print("Loaded!")


@app.route('/ner_extractor')
def ner_extractor():
    return render_template('ner_extractor.html')


@app.route('/ner_extracted_tagging', methods=["GET", "POST"])
def ner_extracted_tagging():
    start = time.time()
    if request.method == 'POST':
        raw_text = request.form['rawtext']

        # Spacy NER Tagger
        start_spacy = time.time()
        nlp_spacy = MODELS['en_core_web_sm']
        docx_spacy = nlp_spacy(raw_text)
        html_spacy = displacy.render(docx_spacy, style="ent")
        html_spacy = html_spacy.replace("\n\n", "\n")
        end_spacy = time.time()
        tagging_gen_time_spacy = end_spacy - start_spacy

        end = time.time()
        final_time = end - start
    return render_template('ner_extracted_tagging.html',
                           rawtext=raw_text,
                           result_spacy=html_spacy,
                           tagging_gen_time_spacy=tagging_gen_time_spacy,
                           final_time=final_time
                           )
