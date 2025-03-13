"""
Flask and server config
Formats a text response using data from EmotionDetection
"""
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")
"""
instantiate flask app with name "Emotion Detection"
"""


@app.route("/emotionDetector")
def emot_analyzer():
    """
    Receives textToAnalyze from user input.  
    Test for valid input (dominant_emotion != None)

    If valid, return formatted results in sentence, otherwise return error message
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] != "None":
        formatted_text = "For the given statement, the system response is "
        keys = list(response.keys())
        i = len(response) - 1
        for k in keys:
            if k != 'dominant_emotion':
                formatted_text += f"'{k}' : {response[k]}"
                i -= 1
                formatted_text += ", " if i > 0 else ". "
            else:
                formatted_text += f"The {k.replace('_', ' ')} is {response[k]}."
    else:
        formatted_text = "Invalid text! Please try again!."
    return formatted_text


@app.route("/")
def render_index_page():
    """
    define route to index page for UI
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
