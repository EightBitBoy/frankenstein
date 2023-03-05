# stream_generator
import json
import logging
import praw
import os
import sys
import time
from kafka import KafkaProducer

print("Hello world!")
time.sleep(5)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

producer = KafkaProducer(
  bootstrap_servers='kafka:9092',
  value_serializer=lambda m: json.dumps(m).encode('utf8'))

client_id_value = open(os.environ["CLIENT_ID_FILE"]).readline().rstrip()
client_secret_value = open(os.environ["CLIENT_SECRET_FILE"]).readline().rstrip()

reddit = praw.Reddit(
    client_id = client_id_value,
    client_secret = client_secret_value,
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
)

for comment in reddit.subreddit("askreddit").stream.comments():
  producer.send('comments',
                {'author': comment.author.name,
                 'text': comment.body,
                 'created': comment.created_utc,
                 'id': comment.id,
                 'score': comment.score})
