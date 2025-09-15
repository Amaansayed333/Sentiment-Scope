import streamlit as st
import pandas as pd
from data_collector import RedditCollector
from sentiment_analyzer import SentimentAnalyzer
from database import SentimentDB
from utils import sentiment_distribution

st.set_page_config(page_title="SentimentScope Dashboard", layout="wide")

collector = RedditCollector()
analyzer = SentimentAnalyzer()
db = SentimentDB()

st.sidebar.title("🎭 Sentiment Dashboard")
keyword = st.sidebar.text_input("Enter keyword", "iPhone 16")

if st.sidebar.button("Fetch & Analyze"):
    posts = collector.fetch_posts(keyword)
    for _, row in posts.iterrows():
        sentiment, score = analyzer.analyze(row["title"] + " " + row["text"])
        db.insert_row((
            row["id"],                 # id
            row["title"],              # text
            sentiment,                 # sentiment
            float(score),              # confidence
            row["timestamp"],          # timestamp
            keyword,                   # keyword
            row["source"]              # source
        ))

rows = db.fetch_all(keyword)
if rows:
    df = pd.DataFrame(rows, columns=["id", "text", "sentiment", "confidence", "timestamp", "keyword", "source"])
    
    st.subheader(f"Results for '{keyword}'")
    st.plotly_chart(sentiment_distribution(df))
    st.dataframe(df[["text", "sentiment", "confidence", "timestamp"]])
