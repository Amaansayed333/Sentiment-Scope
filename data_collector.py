import praw
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class RedditCollector:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT")
        )
    
    def fetch_posts(self, keyword, limit=50):
        posts = []
        for submission in self.reddit.subreddit("all").search(keyword, limit=limit):
            posts.append({
                "id": submission.id,
                "title": submission.title,
                "text": submission.selftext,
                "score": submission.score,
                "timestamp": datetime.fromtimestamp(submission.created_utc),
                "url": submission.url,
                "keyword": keyword,
                "source": "reddit"
            })
        return pd.DataFrame(posts)
