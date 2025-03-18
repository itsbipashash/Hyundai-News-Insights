from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
text = "Hyundai Motors’ related party headache - Finshots"
sentiment_score = analyzer.polarity_scores(text)['compound']

# Classify Sentiment
if sentiment_score > 0:
    sentiment = "Positive"
elif sentiment_score < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Sentiment: {sentiment}")

text = "Stock market live: Hyundai Motor India, Mobikwik, Hero Motocorp hit 52-week low; check details - Upstox"
sentiment_score = analyzer.polarity_scores(text)['compound']

# Classify Sentiment
if sentiment_score > 0:
    sentiment = "Positive"
elif sentiment_score < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Sentiment: {sentiment}")

text = "5 New Compact SUVs Likely Coming In 2025 - Maruti To Hyundai - GaadiWaadi.com"
sentiment_score = analyzer.polarity_scores(text)['compound']

# Classify Sentiment
if sentiment_score > 0:
    sentiment = "Positive"
elif sentiment_score < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Sentiment: {sentiment}")

text = "Extremely relaxing road trip to beautiful Coonoor in our Hyundai i20 - Team-BHP"
sentiment_score = analyzer.polarity_scores(text)['compound']

# Classify Sentiment
if sentiment_score > 0:
    sentiment = "Positive"
elif sentiment_score < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Sentiment: {sentiment}")

text = "Curtains down on this sedan? Long time rival of Honda City, Hyundai Verna - India Today"
sentiment_score = analyzer.polarity_scores(text)['compound']

# Classify Sentiment
if sentiment_score > 0:
    sentiment = "Positive"
elif sentiment_score < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Sentiment: {sentiment}")

text = "Next-Gen Hyundai Creta Hybrid In The Works - Key Details - GaadiWaadi.com"
sentiment_score = analyzer.polarity_scores(text)['compound']

# Classify Sentiment
if sentiment_score > 0:
    sentiment = "Positive"
elif sentiment_score < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Sentiment: {sentiment}")

text = "Hyundai Creta long term review, 9,800km report - Autocar India"
sentiment_score = analyzer.polarity_scores(text)['compound']

# Classify Sentiment
if sentiment_score > 0:
    sentiment = "Positive"
elif sentiment_score < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Sentiment: {sentiment}")

text = "Hyundai Creta Electric SUV's Owner: Mercedes Features, Alto Mileage [Video] - CarToq.com"
sentiment_score = analyzer.polarity_scores(text)['compound']

# Classify Sentiment
if sentiment_score > 0:
    sentiment = "Positive"
elif sentiment_score < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Sentiment: {sentiment}")

text = "Tata Sierra Test Unit Spotted next to Hyundai Creta - CarTrade.com"
sentiment_score = analyzer.polarity_scores(text)['compound']

# Classify Sentiment
if sentiment_score > 0:
    sentiment = "Positive"
elif sentiment_score < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Sentiment: {sentiment}")

text = "shinhan Bank partners with Hyundai Mobis for loan services to suppliers - Korea Economic Daily"
sentiment_score = analyzer.polarity_scores(text)['compound']

# Classify Sentiment
if sentiment_score > 0:
    sentiment = "Positive"
elif sentiment_score < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Sentiment: {sentiment}")