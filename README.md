# Reddit Trading Notifier

Requires [pdotenv](https://pypi.org/project/python-dotenv/), [PRAW](https://praw.readthedocs.io/en/latest/index.html)

Relatively simple script to browse a reddit trading subreddit using the Reddit API and notify the user by email of a particular item on sale within the UK. Project was intended to replace a project that used parsing retrieved html.

ENV_SAMPLE.env requires renaming to .env and contents modified to match API data and email information, current implementation uses gmail
