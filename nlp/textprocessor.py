# https://spacy.io/usage/spacy-101

#Tokenization
#Part-of-speech (POS) Tagging
# python -m spacy download en_core_web_sm

print("Hello world!")

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
for token in doc:
  print(token.text, token.pos_, token.dep_)
