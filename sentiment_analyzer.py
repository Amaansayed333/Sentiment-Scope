from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.model = pipeline("sentiment-analysis", 
                              model="cardiffnlp/twitter-roberta-base-sentiment-latest")
    
    def analyze(self, text):
        try:
            result = self.model(text[:512])[0]  # truncate long text
            return result["label"], float(result["score"])
        except:
            return "NEUTRAL", 0.0
