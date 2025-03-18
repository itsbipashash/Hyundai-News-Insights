import requests
from bs4 import BeautifulSoup
import csv

# Define the search query
query = "Hyundai"

# Google News RSS feed for Hyundai
url = f"https://news.google.com/rss/search?q={query}"

# Make a request to the RSS feed
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "xml")  # Use "xml" for RSS feeds

    # Extract news items
    items = soup.find_all("item")[:10]

    # Store data in a list
    news_data = []
    for item in items:
        title = item.title.text
        link = item.link.text
        news_data.append([title, link])

    # Save to CSV
    with open("Hyundai_news.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Link"])
        writer.writerows(news_data)

    print(f"Scraped {len(news_data)} news articles related to Hyundai and saved to Hyundai_news.csv.")
else:
    print("Failed to retrieve news articles.")





