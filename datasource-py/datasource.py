# stream_generator
import praw
import time
print("Hello world!")

secrets = open("/run/secrets/frankenstein-secrets", "r")
print(secrets.read())


# while(True):
#     time.sleep(3)
#     print("foo")

# reddit = praw.Reddit(
#     client_id="foo",
#     client_secret="bar",
#     user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
# )

# for submission in reddit.subreddit("askreddit").new(limit=3):
#     print(submission.title)
