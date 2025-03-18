import csv
from gtts import gTTS
import os
from playsound import playsound
from deep_translator import GoogleTranslator  # Import Google Translator

# Initialize translator
translator = GoogleTranslator(source="en", target="hi")

# Read news titles from CSV
input_file = "Hyundai_news.csv"

news_titles = []
with open(input_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        news_titles.append(row[0])  # Assuming the first column contains the title

# Convert English news titles to Hindi speech
for i, english_text in enumerate(news_titles[:10], start=1):  # Limiting to 10 articles
    filename = f"news_{i}.mp3"

    # Translate English to Hindi
    hindi_text = translator.translate(english_text)

    # Convert to speech and save
    tts = gTTS(text=hindi_text, lang="hi", slow=False)
    tts.save(filename)

    print(f"Playing: {hindi_text}")  # Show Hindi text being played
    playsound(filename)  # Play the speech

    os.remove(filename)  # Delete the file after playing to save space



