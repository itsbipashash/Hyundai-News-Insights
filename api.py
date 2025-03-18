from fastapi import FastAPI
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator
from gtts import gTTS

app = FastAPI()

CSV_FILE = "Hyundai_news.csv"

# Load news data
def load_news():
    try:
        return pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        return None

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

@app.get("/")
def home():
    return {"message": "Welcome to News Sentiment API"}

@app.get("/get_news/")
def get_news():
    """Fetch news articles from CSV"""
    df = load_news()
    if df is None:
        return {"error": "No news data available."}
    return df.to_dict(orient="records")

@app.get("/analyze_sentiment/")
def analyze_sentiment():
    """Perform sentiment analysis on news headlines"""
    df = load_news()
    if df is None:
        return {"error": "No news data available."}

    df["Sentiment"] = df["Title"].apply(lambda text: "Positive" if analyzer.polarity_scores(text)["compound"] > 0
                                        else "Negative" if analyzer.polarity_scores(text)["compound"] < 0
                                        else "Neutral")

    return df[["Title", "Sentiment"]].to_dict(orient="records")

@app.get("/text_to_speech/{news_index}")
def text_to_speech(news_index: int):
    """Convert a specific news headline to Hindi speech"""
    df = load_news()
    if df is None or news_index >= len(df):
        return {"error": "Invalid news index"}

    title = df.iloc[news_index]["Title"]
    hindi_text = GoogleTranslator(source="en", target="hi").translate(title)

    # Convert text to speech
    filename = f"news_{news_index}.mp3"
    tts = gTTS(text=hindi_text, lang="hi", slow=False)
    tts.save(filename)

    return {"message": "Speech generated", "hindi_text": hindi_text, "audio_file": filename}

