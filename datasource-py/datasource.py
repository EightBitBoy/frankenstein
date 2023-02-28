# stream_generator
import logging
import praw
import os
import sys

print("Hello world!")

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

client_id_value = open(os.environ["CLIENT_ID_FILE"]).readline().rstrip()
client_secret_value = open(os.environ["CLIENT_SECRET_FILE"]).readline().rstrip()

reddit = praw.Reddit(
    client_id = client_id_value,
    client_secret = client_secret_value,
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
)

# for submission in reddit.subreddit("askreddit").new(limit=3):
#     print(submission.title)


for comment in reddit.subreddit("askreddit").stream.comments():
    logging.info(comment.author)
