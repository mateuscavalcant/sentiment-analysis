from flask import Flask, render_template, request, json
from server.analysis import analyze_sentiment


app = Flask(__name__)

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for analyzing sentiment
@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment_route():
    # Get the content from the request
    content = request.json.get("content", "")

    # Analyze the sentiment of the content
    sentiment = analyze_sentiment(content)

    # Send the sentiment result back to the client
    response = json.dumps({"sentiment": sentiment})
    return response


if __name__ == "__main__":
    # Run the Flask app
    app.run(host='0.0.0.0', port=8765, debug=True, threaded=True)
