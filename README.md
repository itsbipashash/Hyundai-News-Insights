# Hyundai-News-Insights
# Overview
This web application extracts Hyundai-related news articles, performs sentiment analysis, and converts summarized content into Hindi speech. It provides a user-friendly Streamlit interface for interactive exploration of news sentiment trends.

# Features
 News Extraction – Scrapes Hyundai-related articles from Google News RSS.
 Sentiment Analysis – Uses VADER to classify sentiment as Positive, Negative, or Neutral.
 Comparative Sentiment Analysis – Aggregates sentiment results for trend insights.
 Hindi Text-to-Speech (TTS) – Converts news headlines into Hindi audio using gTTS.
 Web UI (Streamlit) – Users can view news, sentiment analysis, and listen to Hindi speech.
 REST API (FastAPI) – Allows programmatic access to news and sentiment data.
 
 # Install dependencies:
   pip install -r requirements.txt

# Run Streamlit app:
  streamlit run app.py
# Technologies Used
  Python – Backend logic
  BeautifulSoup – Web scraping
  VADER Sentiment Analysis – Text sentiment detection
  Google Translate & gTTS – Hindi translation & speech synthesis
  Streamlit – Web UI
  FastAPI – API backend
