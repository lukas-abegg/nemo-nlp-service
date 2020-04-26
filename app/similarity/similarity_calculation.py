from app import app

from flask import render_template, request
from app.spacy.spacy_models import MODELS

import time


@app.route('/similarity')
def similarity():
    return render_template('similarity.html')


def calculate_sims(nlp, texts: list):
    doc1 = nlp(texts[0])
    doc2 = nlp(texts[1])
    doc3 = nlp(texts[2])

    sim1_bert = (doc1[0].similarity(doc2[0]))
    sim2_bert = (doc1[0].similarity(doc3[0]))
    sim3_bert = (doc2[0].similarity(doc3[0]))

    return [sim1_bert, sim2_bert, sim3_bert]


@app.route('/similarity_calculated', methods=["GET", "POST"])
def similarity_calculated():
    start = time.time()
    if request.method == 'POST':
        raw_text1 = request.form['rawtext1']
        raw_text2 = request.form['rawtext2']
        raw_text3 = request.form['rawtext3']

        lang = request.form['lang']

        if lang == "de":
            lang_text = "German"
            nlp_bert = MODELS['de_trf_bertbasecased_lg']
            nlp_spacy = MODELS['de_core_news_sm']
        else:
            lang_text = "English"
            nlp_bert = MODELS['en_trf_bertbaseuncased_lg']
            nlp_spacy = MODELS['en_core_web_sm']

        raw_texts = [raw_text1, raw_text2, raw_text3]

        # Bert
        sims_bert = calculate_sims(nlp_bert, raw_texts)

        # Spacy
        sims_spacy = calculate_sims(nlp_spacy, raw_texts)

        end = time.time()
        final_time = end - start
    return render_template('similarity_calculated.html',
                           texts=raw_texts,
                           sims_bert=sims_bert,
                           sims_spacy=sims_spacy,
                           final_time=final_time,
                           lang=lang_text
                           )
