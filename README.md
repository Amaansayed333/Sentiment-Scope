# Sentiment-Scope
A real-time sentiment analysis dashboard that monitors social media mentions and provides actionable insights through interactive visualizations. Built with HuggingFace Transformers, FastAPI, and Streamlit for scalable sentiment monitoring across multiple platforms.

## 📸 Demo Screenshot
![Dashboard Screenshot](result-1.png)

🛠️ Tech Stack
Backend

Python 3.8+ - Core programming language
HuggingFace Transformers - Pre-trained NLP models
PRAW - Reddit API wrapper
SQLite/PostgreSQL - Data storage
Pandas - Data manipulation

Frontend

Streamlit - Interactive web dashboard
Plotly - Dynamic visualizations
WordCloud - Text visualization

ML Models

cardiffnlp/twitter-roberta-base-sentiment - Primary sentiment model
VADER Sentiment - Social media optimized analyzer
TextBlob - Baseline comparison model

Deployment

Streamlit Cloud - Free hosting
GitHub Actions - CI/CD pipeline
Docker - Containerization (optional)

⚡ Setup Instructions

1.Clone the repo
git clone https://github.com/Amaansayed333/Sentiment-Scope.git
cd Sentiment-Scope

2.Create Virtual Environment
python -m venv myenv
myenv\Scripts\activate     # Windows
source myenv/bin/activate  # Linux / Mac

3.Install dependencies
pip install -r requirements.txt

4.Setup Reddit API Credentials
Create an app at Reddit Apps
Copy client_id, client_secret, user_agent
Create .env file:

REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent

5.Run the dashboard
streamlit run app.py
