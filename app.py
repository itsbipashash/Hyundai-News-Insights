import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# Load News Data
CSV_FILE = "Hyundai_news.csv"

@st.cache_data
def load_news_data():
    try:
        df = pd.read_csv(CSV_FILE)
        return df
    except FileNotFoundError:
        return None

# Function for Sentiment Analysis
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)['compound']
    if score > 0:
        return "Positive", score
    elif score < 0:
        return "Negative", score
    else:
        return "Neutral", score

# Function for Hindi Text-to-Speech
def generate_speech(text, index):
    translator = GoogleTranslator(source="en", target="hi")
    hindi_text = translator.translate(text)
    filename = f"news_{index}.mp3"
    tts = gTTS(text=hindi_text, lang="hi", slow=False)
    tts.save(filename)
    return filename, hindi_text

# Streamlit UI
st.title("Company News Sentiment Analyzer")

# Company Selection
company_name = st.selectbox("Select a Company", ["Hyundai"])  # Add more companies if needed

# Load News Data
df = load_news_data()

if df is None:
    st.error("No news data available. Please upload `Hyundai_news.csv`.")
else:
    st.write(f"Showing latest news articles for **{company_name}**:")

    # Analyze Sentiment for each article
    df["Sentiment"], df["Sentiment Score"] = zip(*df["Title"].apply(analyze_sentiment))

    # Display results
    for i, row in df.iterrows():
        st.subheader(row["Title"])
        st.write(f"🔗 [Read More]({row['Link']})")
        st.write(f"📝 Sentiment: **{row['Sentiment']}** (Score: {row['Sentiment Score']})")

        # Convert to Hindi Speech
        if st.button(f"🔊 Listen in Hindi ({i+1})", key=f"btn_{i}"):
            speech_file, hindi_translation = generate_speech(row["Title"], i)
            st.audio(speech_file, format="audio/mp3")
            st.write(f"🗣️ **Hindi Translation:** {hindi_translation}")

    # Save Updated Sentiment Data
    df.to_csv("Hyundai_news_sentiment.csv", index=False)
    st.success("Sentiment analysis completed! Results saved.")
if __name__ == "__main__":
    st.write("Starting Streamlit App...")
