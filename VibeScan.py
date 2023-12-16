import nltk
import tkinter as tk
from tkinter import Toplevel

# nltk.download('vader_lexicon')
# nltk.download('punkt')

from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment():
    text = text_input.get("1.0", "end-1c")
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    result_label.config(text=str(sentiment))

    # Detailed Breakdown Window
    detail_window = Toplevel(root)
    detail_window.title("Detailed Breakdown")

    # Format and display detailed breakdown
    details = f"Positive: {sentiment['pos']}\n"
    details += f"Neutral: {sentiment['neu']}\n"
    details += f"Negative: {sentiment['neg']}\n"
    details += f"Compound: {sentiment['compound']}"

root = tk.Tk()
root.title("Sentiment Analysis App")

text_input = tk.Text(root, height=10, width=50)
text_input.pack()

analyze_button = tk.Button(root, text="Analyze", command=analyze_sentiment)
analyze_button.pack()

result_label = tk.Label(root, text="Sentiment Analysis Results")
result_label.pack()

root.mainloop()