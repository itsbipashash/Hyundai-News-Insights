import pandas as pd

# List of Sentiments from sentiment analysis
sentiments = [
    "Positive", "Positive", "Neutral", "Positive", "Neutral",
    "Neutral", "Neutral", "Neutral", "Neutral", "Neutral"
]

# Convert to DataFrame
df = pd.DataFrame(sentiments, columns=["Sentiment"])

# Count the occurrences of each sentiment
sentiment_counts = df["Sentiment"].value_counts()

# Print sentiment distribution
print("Sentiment Distribution:")
print(sentiment_counts)
