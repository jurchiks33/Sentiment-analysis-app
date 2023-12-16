import nltk

nltk.download('vader_lexicon')
nltk.download('punkt')

from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment

user_input = input("Enter a sentence for sentiment analysis: ")
result = analyze_sentiment(user_input)
print("Sentiment Analysis:", result)