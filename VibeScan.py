import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from googletrans import Translator
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter

translator = Translator()
sia = SentimentIntensityAnalyzer()

chart = None
canvas = None

#Emotion lexicon for manual emotional analysis
emotion_lexicon = {
    "happy": [
        "happy", "jouful", "pleased", "delighted", "estatic", 
        "cheerful", "content", "glad", "satisfied", "thrilled", 
        "elated", "overjoyed", "beaming", "buoyant", "jubilant"
    ],
    "sad": [
        "sad", "downcast", "mournful", "upset", "depressed", 
        "sorrowful", "gloomy", "heartbroken", "tearful", "melancholy", 
        "dismal", "despondent", "disheartened", "forlorn", "woeful"
    ],
    "angry": [
        "angry", "mad", "furious", "irritated", "annoyed", 
        "enraged", "irate", "livid", "outraged", "wrathful", 
        "heated", "exasperated", "vexed", "indignant", "agitated"
    ],
    "surprise": [
        "surprised", "amazed", "astonished", "shocked", "stunned",
        "astounded", "flabbergasted", "startled", "dumbfounded", "bewildered", 
        "taken aback", "agog", "awestruck", "thunderstruck", "stupefied"
    ],
    "fear": [
        "fearful", "scared", "terrified", "afraid", "panic", 
        "frightened", "alarmed", "petrified", "horrified", "dread", 
        "trepidation", "anxious", "nervous", "apprehensive", "timid"
    ]
}

def analyze_emotion(text):
    tokens = text.lower().split()
    emotion_counts = {emotion: 0 for emotion in emotion_lexicon}
    for word in tokens:
        for emotion, words in emotion_lexicon.items():
            if word in words:
                emotion_counts[emotion] += 1
    predominant_emotion, _= Counter(emotion_counts). most_common(1)[0]
    return predominant_emotion, emotion_counts


def analyze_sentiment():
    global chart, canvas

    text = text_input.get("1.0", "end-1c")
    
    # Translate the text to English
    translated_text = translator.translate(text, src='lv', dest='en').text

    sentiment = sia.polarity_scores(translated_text)
    sentiment_result_label.config(text="Sentiment Analysis Results: " + str(sentiment)) 

    # Data for pie chart
    labels = ['Positive', 'Neutral', 'Negative']
    sizes = [sentiment['pos'], sentiment['neu'], sentiment['neg']]
    colors = ['green', 'blue', 'red']

    update_chart(sizes, labels, colors)

def analyze_emotion_event():
    global chart, canvas

    text = text_input.get("1.0", "end-1c")
    translated_text = translator.translate(text, src='lv', dest='en').text

    predominant_emotion, emotion_counts = analyze_emotion(translated_text)
    emotion_result_label.config(text=f"Emotion Analysis Results: {predominant_emotion} {emotion_counts}")

    # Data for emotion pie chart
    labels = list(emotion_counts.keys())
    sizes = list(emotion_counts.values())
    colors = ['yellow', 'red', 'green', 'blue', 'orange']

    update_chart(sizes, labels, colors)


def update_chart(sizes, labels, colors):
    global canvas

    if canvas is not None:
        canvas.figure.clf()
        ax = canvas.figure.subplots()
    else:
        fig, ax = plt.subplots()
    
    if not any(sizes):
        print("No data to display: all sizes are zero.")
        if canvas is not None:
            canvas.draw()
        return
    
    ax.pie(sizes, labels= labels, colors= colors, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')

    if canvas is not None:
        canvas.draw()
    else:
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

root = tk.Tk()
root.title("VibeScan: Sentiment and Emotion Analysis App")

# Calculate window size and position
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.3)
window_height = int(screen_height * 0.6)
position_right = int(screen_width / 2 - window_width / 2)
position_down = int(screen_height / 2 - window_height / 2)

# Set window size and position
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

text_input = tk.Text(root, height=10, width=50)
text_input.pack()

analyze_sentiment_button = tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_sentiment_button.pack()

sentiment_result_label = tk.Label(root, text="Sentiment Analysis Results")
sentiment_result_label.pack()

analyze_emotion_button = tk.Button(root, text="Analyze Emotion", command=analyze_emotion_event)
analyze_emotion_button.pack()

emotion_result_label = tk.Label(root, text="Emotion Analysis Results")
emotion_result_label.pack()

root.mainloop()



# need to fix AttributeError: module 'emoji' has no attribute 'UNICODE_EMOJI'
#need to try different python package or API-based solutions.
# As a temporary measure comment out parts of code to check if other code parts
#are working properly.