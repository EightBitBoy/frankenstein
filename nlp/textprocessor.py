# https://spacy.io/usage/spacy-101

#Tokenization
#Part-of-speech (POS) Tagging
# python -m spacy download en_core_web_sm
import json
import spacy
from kafka import KafkaProducer
from kafka import KafkaConsumer

print("Hello world!")

consumer = KafkaConsumer(
  'comments',
  bootstrap_servers=['kafka:9092'],
  value_deserializer=lambda m: json.loads(m.decode('utf8')))
producer = KafkaProducer(bootstrap_servers='kafka:9092')

for message in consumer:
  print(message.value["author"])
  # print(type(message.value["author"]))
  # print(json.loads(message.value).author)

# nlp = spacy.load("en_core_web_sm")
# doc = nlp("My beautiful wife is working at the computer.")
# for token in doc:
#   print(token.text, )
#   producer.send(token.pos_.lower(), token.text.encode())
