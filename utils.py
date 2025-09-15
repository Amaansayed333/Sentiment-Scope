import plotly.express as px
import pandas as pd

def sentiment_distribution(df):
    counts = df["sentiment"].value_counts()
    fig = px.pie(values=counts.values, names=counts.index, title="Sentiment Distribution")
    return fig
