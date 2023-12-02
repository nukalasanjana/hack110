# train_model.py

import spacy

nlp = spacy.load("en_core_web_sm")

training_data = [
    ("Hello, how are you?", {"intent": "greeting"}),
    ("Tell me a joke.", {"intent": "joke"}),
]

for text, annotations in training_data:
    doc = nlp(text)
    for word in doc:
        if word.is_alpha:
            annotations.setdefault("entities", []).append((word.idx, word.idx + len(word.text), "WORD"))


nlp.to_disk("chatbot_model")