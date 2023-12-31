import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from googletrans import Translator
from nltk.sentiment import SentimentIntensityAnalyzer
import text2emotion as te

translator = Translator()
sia = SentimentIntensityAnalyzer()

chart = None
canvas = None

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

def analyze_emotion():
    global chart, canvas

    text = text_input.get("1.0", "end-1c")
    translated_text = translator.translate(text, src='lv', dest='en').text

    emotion = te.get_emotion(translated_text)
    emotion_result_label.config(text="Emotion Analysis Results: " + str(emotion))

    # Data for emotion pie chart
    labels = list(emotion.keys())
    sizes = list(emotion.values())
    colors = ['yellow', 'red', 'green', 'blue', 'orange']

    update_chart(sizes, labels, colors)



def update_chart(sizes, labels, colors):
    global chart, canvas

    # Clear the previous pie chart
    if chart is not None:
        for piece in chart[0]:
            piece.remove()

    # Create figure for the pie chart
    fig, ax = plt.subplots()
    chart = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


    # Embedding the pie chart into the Tkinter window
    if canvas is not None:
        canvas.get_tk_widget().destroy()
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

analyze_emotion_button = tk.Button(root, text="Analyze Emotion", command=analyze_emotion)
analyze_emotion_button.pack()

emotion_result_label = tk.Label(root, text="Emotion Analysis Results")
emotion_result_label.pack()

root.mainloop()



# need to fix AttributeError: module 'emoji' has no attribute 'UNICODE_EMOJI'
#need to try different python package or API-based solutions.
# As a temporary measure comment out parts of code to check if other code parts
#are working properly.