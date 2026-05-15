# IMPORT LIBRARIES
import spacy
from spacy.training.example import Example
import random
import shutil

# STEP 1: CREATE BLANK ENGLISH MODEL
nlp = spacy.blank("en")

# STEP 2: ADD NER PIPELINE
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
else:
    ner = nlp.get_pipe("ner")

# STEP 3: ADD CUSTOM LABELS
labels = ["CROP", "DISEASE", "SYMPTOM", "CHEMICAL"]

for label in labels:
    ner.add_label(label)

# STEP 4: TRAINING DATA
TRAIN_DATA = [
    ("Wheat has rust disease",
     {"entities": [(0, 5, "CROP"), (10, 22, "DISEASE")]}),

    ("Rice suffers from blast disease",
     {"entities": [(0, 4, "CROP"), (19, 32, "DISEASE")]}),

    ("Farmer used pesticide on crops",
     {"entities": [(13, 23, "CHEMICAL")]}),

    ("Plants show yellow leaves",
     {"entities": [(12, 25, "SYMPTOM")]}),

    ("Maize is affected by fungal infection",
     {"entities": [(0, 5, "CROP"), (22, 38, "DISEASE")]})
]

# STEP 5: TRAIN MODEL
optimizer = nlp.begin_training()

for epoch in range(10):

    random.shuffle(TRAIN_DATA)
    losses = {}

    for text, annotations in TRAIN_DATA:

        doc = nlp.make_doc(text)

        example = Example.from_dict(doc, annotations)

        nlp.update([example], losses=losses)

    print(f"Epoch {epoch+1} Loss: {losses}")

# STEP 6: SAVE MODEL
nlp.to_disk("custom_ner_model")

print("\nModel Trained Successfully!")

# STEP 7: TEST MODEL
test_text = "Wheat has fungal infection"

doc = nlp(test_text)

print("\nDetected Entities:")

for ent in doc.ents:
    print(ent.text, "->", ent.label_)

# STEP 8: CREATE ZIP FILE
shutil.make_archive("custom_ner_model", 'zip', "custom_ner_model")

print("\nZIP File Created Successfully!")