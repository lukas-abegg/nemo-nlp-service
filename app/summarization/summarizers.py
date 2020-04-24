from __future__ import unicode_literals
from flask import render_template, request, flash, redirect, url_for

from app import app

from app.spacy.spacy_models import MODELS

from app.summarization.spacy_summarization import text_summarizer
from gensim.summarization.summarizer import summarize
from app.summarization.nltk_summarization import nltk_summarizer
from app.summarization.sumy_summarization import sumy_summary

import time

nlp = MODELS['en_core_web_sm']


# Reading Time
def reading_time(mytext):
    total_words = len([token.text for token in nlp(mytext)])
    estimated_time = total_words / 200.0
    return estimated_time


def check_sentence_amount(text: str) -> bool:
    return len([sent.text for sent in nlp(text).sents]) < 2


@app.route('/summarization')
def summarization():
    return render_template('summarization.html')


@app.route('/summarization_extracted', methods=['GET', 'POST'])
def summarization_extracted():
    start = time.time()

    if request.method == 'POST':
        rawtext = request.form['rawtext']

        if check_sentence_amount(rawtext):
            flash("It needs at least 2 sentence to summarize")
            return redirect(url_for('summarization'))

        final_reading_time = reading_time(rawtext)
        final_summary_spacy = text_summarizer(rawtext)
        summary_reading_time = reading_time(final_summary_spacy)
        # Gensim Summarizer
        final_summary_gensim = summarize(rawtext)
        summary_reading_time_gensim = reading_time(final_summary_gensim)
        # NLTK
        final_summary_nltk = nltk_summarizer(rawtext)
        summary_reading_time_nltk = reading_time(final_summary_nltk)
        # Sumy
        final_summary_sumy = sumy_summary(rawtext)
        summary_reading_time_sumy = reading_time(final_summary_sumy)

        end = time.time()
        final_time = end - start
    return render_template('summarization_extracted.html',
                           ctext=rawtext,
                           final_summary_spacy=final_summary_spacy,
                           final_summary_gensim=final_summary_gensim, final_summary_nltk=final_summary_nltk,
                           final_time=final_time, final_reading_time=final_reading_time,
                           summary_reading_time=summary_reading_time,
                           summary_reading_time_gensim=summary_reading_time_gensim,
                           final_summary_sumy=final_summary_sumy, summary_reading_time_sumy=summary_reading_time_sumy,
                           summary_reading_time_nltk=summary_reading_time_nltk
                           )
