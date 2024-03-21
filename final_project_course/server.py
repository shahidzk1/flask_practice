"""
Flask application for emotion detection
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

APP = Flask("Emotion Detector")

@APP.route("/emotionDetector")
def sent_analyzer():
    """
    Function to analyze sentiment
    """
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    if emotions['dominant_emotion'] is None:
        return "Invalid input ! Try again."
    dominant_emotion = emotions.pop('dominant_emotion')
    emotions_list = ', '.join([f"'{k}': {v}" for k, v in emotions.items()])
    return (
    f"For the given statement, the system response is {emotions_list}. "
    f"The dominant emotion is {dominant_emotion}."
)

@APP.route("/")
def render_index_page():
    """
    Function to render index page
    """
    return render_template('index.html')

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
