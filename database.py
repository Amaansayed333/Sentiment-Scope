import sqlite3
import pandas as pd

class SentimentDB:
    def __init__(self, db_path="sentiment.db"):
        self.db_path = db_path
        self.init_db()
    
    def connect(self):
        return sqlite3.connect(self.db_path)
    
    def init_db(self):
        conn = self.connect()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS sentiment_data (
                id TEXT PRIMARY KEY,
                text TEXT,
                sentiment TEXT,
                confidence REAL,
                timestamp TEXT,
                keyword TEXT,
                source TEXT
            )
        ''')
        conn.commit()
        conn.close()
    

    def insert_row(self, row):
        conn = self.connect()
        cursor = conn.cursor()

        # Convert Pandas Timestamp → string (ISO format)
        row = list(row)
        for i, val in enumerate(row):
            if isinstance(val, pd.Timestamp):
                row[i] = val.isoformat()

        cursor.execute('''
            INSERT OR REPLACE INTO sentiment_data
            (id, text, sentiment, confidence, timestamp, keyword, source)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', tuple(row))

        conn.commit()
        conn.close()

    
    def fetch_all(self, keyword):
        conn = self.connect()
        rows = conn.execute(
            "SELECT * FROM sentiment_data WHERE keyword=?",
            (keyword,)
        ).fetchall()
        conn.close()
        return rows
