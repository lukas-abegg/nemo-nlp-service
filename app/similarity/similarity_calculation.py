from app import app

from flask import render_template, request
from app.spacy.spacy_models import MODELS

import time


@app.route('/similarity')
def similarity():
    return render_template('similarity.html')


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
            nlp_bert = MODELS['de_trf_bertbaseuncased_lg']
            nlp_spacy = MODELS['de_core_news_sm']
        else:
            lang_text = "English"
            nlp_bert = MODELS['en_trf_bertbaseuncased_lg']
            nlp_spacy = MODELS['en_core_web_sm']

        # Bert
        doc1 = nlp_bert(raw_text1)
        doc2 = nlp_bert(raw_text2)
        doc3 = nlp_bert(raw_text3)
        sim1_bert = (doc1[0].similarity(doc2[0]))
        sim2_bert = (doc1[0].similarity(doc3[0]))
        sim3_bert = (doc2[0].similarity(doc3[0]))

        # Spacy
        doc1 = nlp_spacy(raw_text1)
        doc2 = nlp_spacy(raw_text2)
        doc3 = nlp_spacy(raw_text3)
        sim1_spacy = (doc1[0].similarity(doc2[0]))
        sim2_spacy = (doc1[0].similarity(doc3[0]))
        sim3_spacy = (doc2[0].similarity(doc3[0]))

        end = time.time()
        final_time = end - start
    return render_template('similarity_calculated.html',
                           text1=raw_text1,
                           text2=raw_text2,
                           text3=raw_text3,
                           sim1_bert=sim1_bert,
                           sim2_bert=sim2_bert,
                           sim3_bert=sim3_bert,
                           sim1_spacy=sim1_spacy,
                           sim2_spacy=sim2_spacy,
                           sim3_spacy=sim3_spacy,
                           final_time=final_time,
                           lang=lang_text
                           )
