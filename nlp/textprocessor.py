# https://spacy.io/usage/spacy-101

#Tokenization
#Part-of-speech (POS) Tagging
# python -m spacy download en_core_web_sm
import json
import spacy
import time
from kafka import KafkaProducer
from kafka import KafkaConsumer

print("Hello world!")
time.sleep(5)

consumer = KafkaConsumer(
  'comments',
  bootstrap_servers=['kafka:9092'],
  value_deserializer=lambda m: json.loads(m.decode('utf8')))

producer = KafkaProducer(bootstrap_servers='kafka:9092')

nlp = spacy.load("en_core_web_sm")

for message in consumer:
  doc = nlp(message.value["text"])
  for token in doc:
    producer.send(token.pos_.lower(), token.text.encode())
