import nltk

# nltk.download('vader_lexicon')
# nltk.download('punkt')

from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment():
    text = text_input.get("1.0", "end-1c")
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    result_label.config(text=str(sentiment))

root = tk.Tk()
root.title("Sentiment Analysis App")

text_input = tk.Text(root, height=10, width=50)
text_input.pack()
