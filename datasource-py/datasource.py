# stream_generator
import praw
import os

print("Hello world!")

client_id_value = open(os.environ["CLIENT_ID_FILE"]).readline().rstrip()
client_secret_value = open(os.environ["CLIENT_SECRET_FILE"]).readline().rstrip()

reddit = praw.Reddit(
    client_id = client_id_value,
    client_secret = client_secret_value,
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
)

for submission in reddit.subreddit("askreddit").new(limit=3):
    print(submission.title)
