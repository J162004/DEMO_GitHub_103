from fastapi import FastAPI
import spacy

# LOAD TRAINED MODEL
nlp = spacy.load("custom_ner_model")

# CREATE FASTAPI APP
app = FastAPI()

# HOME ROUTE
@app.get("/")
def home():
    return {"message": "NER API is running"}

# PREDICTION ROUTE
@app.post("/predict")
def predict(data: dict):

    text = data["text"]

    doc = nlp(text)

    entities = []

    for ent in doc.ents:

        entities.append({
            "text": ent.text,
            "label": ent.label_
        })

    return {"entities": entities}