"""starts the server"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods = ["GET"])
def sent_detection():
    """executes the detector function and creates an output"""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        output = "Invalid text! Please try again!"
        return output

    output = (
    f'For the given statement, the system response is '
    f'"anger": {response["anger"]}, '
    f'"disgust": {response["disgust"]}, '
    f'"fear": {response["fear"]}, '
    f'"joy": {response["joy"]} and '
    f'"sadness": {response["sadness"]}. '
    f'The dominant emotion is {response["dominant_emotion"]}.'
    )
    return output

@app.route("/")
def render_index_page():
    """shows the index page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
