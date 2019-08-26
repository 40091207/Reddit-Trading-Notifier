import praw
import dotenv
import os
import re
import Submission
from Submission import Submission
from dotenv import load_dotenv
from os.path import join, dirname

#Praw Documentation - https://praw.readthedocs.io/en/latest/getting_started/quick_start.html
#Reddit Auth - https://www.reddit.com/prefs/apps/
#User Agent format - <platform>:<app ID>:<version string> (by /u/<Reddit username>)

#Load .env enviroment variable file and then read the required parameters
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
env_secret_key = os.environ.get("SECRET_KEY")
env_client_id = os.environ.get("CLIENT_ID")
env_user_agent = os.environ.get("USER_AGENT")

#setup PRAW API parameters
reddit = praw.Reddit(client_id=env_client_id,
                     client_secret=env_secret_key,
                     user_agent=env_user_agent)

#pull first 50 hot submissions from /r/mechmarket using a read_only instance
results = []
for submission in reddit.subreddit('mechmarket').hot(limit=100):
    match = re.match(r'\[EU-UK\].*', str(submission.title))
    if match:
        submission_obj = Submission(submission.id,submission.title,submission.comments)
        results.append(submission_obj)

for z in results:
    print(z.title)
