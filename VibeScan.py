import nltk
import tkinter as tk
from tkinter import Toplevel
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# nltk.download('vader_lexicon')
# nltk.download('punkt')

from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment():
    text = text_input.get("1.0", "end-1c")
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    result_label.config(text=str(sentiment))

    # Data for pie chart
    labels = ['Positive', 'Neutral', 'Negative']
    sizes = [sentiment['pos'], sentiment['neu'], sentiment['neg']]
    colors = ['green', 'blue', 'red']

    # Create figure for the pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


root = tk.Tk()
root.title("Sentiment Analysis App")

text_input = tk.Text(root, height=10, width=50)
text_input.pack()

analyze_button = tk.Button(root, text="Analyze", command=analyze_sentiment)
analyze_button.pack()

result_label = tk.Label(root, text="Sentiment Analysis Results")
result_label.pack()

root.mainloop()