from app import app

from flask import render_template, request
from spacy import displacy
from scispacy.umls_linking import UmlsEntityLinker

from app.spacy.spacy_models import MODELS

import time

print("Loading UMLS Tagger...")
nlp_umls = MODELS['en_core_sci_sm']
linker = UmlsEntityLinker(resolve_abbreviations=False)
nlp_umls.add_pipe(linker)
print("UMLS Tagger loaded!")

@app.route('/med_tagger')
def med_tagger():
    return render_template('med_tagger.html')


def link_to_UMLS(text: str):
    doc = nlp_umls(text)
    entities = [entity for entity in doc.ents]
    entities_final = []
    if len(entities):
        umls_entries = [entity._.umls_ents[0] for entity in entities if len(entity._.umls_ents)]
        if len(umls_entries):
            linked_ents = [linker.umls.cui_to_entity[entity[0]] for entity in umls_entries]
            entities_final = [[entity.canonical_name, entity.definition] for entity in linked_ents]
    return entities_final


def render_entities_tagged(nlp, text: str):
    docx_core = nlp(text)
    html_core = displacy.render(docx_core, style="ent")
    return html_core.replace("\n\n", "\n")


@app.route('/med_tagger_extracted', methods=["GET", "POST"])
def med_tagger_extracted():
    start = time.time()
    if request.method == 'POST':
        raw_text = request.form['rawtext']

        # en_core_sci_sm
        start_core = time.time()

        nlp_core = MODELS['en_core_sci_sm']
        html_core = render_entities_tagged(nlp_core, raw_text)
        end_core = time.time()
        tagging_gen_time_core = end_core - start_core

        umls_entries = link_to_UMLS(raw_text)

        # en_ner_bc5cdr_md
        start_spacy = time.time()
        nlp_spacy = MODELS['en_ner_bc5cdr_md']
        html_spacy = render_entities_tagged(nlp_spacy, raw_text)
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
                           umls_entries=umls_entries,
                           final_time=final_time
                           )
