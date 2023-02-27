# stream_generator
print("Hello world!")

import praw

reddit = praw.Reddit(
    client_id="foo",
    client_secret="bar",
    user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
)

for submission in reddit.subreddit("askreddit").new(limit=3):
    print(submission.title)
