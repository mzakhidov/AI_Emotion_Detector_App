from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    This function handles the '/emotionDetector' route. 
    It receives a query parameter 'textToAnalyze' 
    from the request, passes it to the emotion_detector function 
    to get the emotion analysis, and returns 
    a formatted response with the emotion scores and the dominant emotion. 
    If the dominant emotion is None, 
    it returns an error message.

    Returns:
        str: A formatted string with the emotion analysis or 
        an error message if dominant_emotion is None.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion_detector function to analyze the text and get the emotions
    response = emotion_detector(text_to_analyze)

    # Extract emotion scores from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']

    # Check if dominant_emotion is None and return an error message
    if dominant is None:
        return "Invalid text! Please try again."

    # Return the emotion analysis in a formatted string
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

@app.route("/")
def render_index_page():
    """
    This function handles the root route '/'. 
    It renders the index.html template for the landing page.

    Returns:
        str: The rendered index.html page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    """
    The entry point for running the Flask application. 
    It starts the app on host '0.0.0.0' and port 5000.

    Runs:
        app: Starts the Flask application server.
    """
    app.run(host="0.0.0.0", port=5000)
