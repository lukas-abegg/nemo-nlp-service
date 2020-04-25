import spacy

print("Loading...")
MODELS = {
    "en_core_web_sm": spacy.load("en_core_web_sm"),
    "de_core_news_sm": spacy.load("de_core_news_sm"),
    "en_core_sci_sm": spacy.load("en_core_sci_sm"),
    "en_ner_bc5cdr_md": spacy.load("en_ner_bc5cdr_md"),
    "de_trf_bertbasecased_lg": spacy.load("de_trf_bertbasecased_lg"),
    "en_trf_bertbaseuncased_lg": spacy.load("en_trf_bertbaseuncased_lg")
}
print("Loaded!")
