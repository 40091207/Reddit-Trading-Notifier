import praw
import dotenv
import os
import re
import Submission
import Email
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
env_sender_email = os.environ.get("SENDER_EMAIL")
env_sender_pw = os.environ.get("SENDER_PW")
env_reciever_email = os.environ.get("RECIEVER_EMAIL")

#setup PRAW API parameters
reddit = praw.Reddit(client_id=env_client_id,
                     client_secret=env_secret_key,
                     user_agent=env_user_agent)

#pull first 50 hot submissions from /r/mechmarket using a read_only instance
#match all results from the UK
results = []
for submission in reddit.subreddit('mechmarket').hot(limit=200):
    location_match = re.match(r'\[EU-UK\].*', str(submission.title))
    if location_match and 'koi' in submission.title.lower():
        submission_obj = Submission(submission.id,submission.title,submission.comments, submission.URL)
        results.append(submission_obj)

#if any matching results are discovered send url in email
if len(results) != 0:
        for result in results:
                Email.send_email(env_sender_email, env_sender_pw, env_reciever_email, 'RedditBot', 'Reddit thread meets requirement: ' + result.url)