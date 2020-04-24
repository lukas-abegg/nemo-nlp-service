import spacy

print("Loading...")
MODELS = {
    "en_core_web_sm": spacy.load("en_core_web_sm"),
    "en_trf_bertbaseuncased_lg": spacy.load("en_trf_bertbaseuncased_lg")
}
print("Loaded!")
