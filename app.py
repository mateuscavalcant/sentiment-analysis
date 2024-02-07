from server.analysis import analyze_sentiment
from flask import Flask, request, render_template, json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment_route():
    content = request.json.get("content", "")

    # Analyze the sentiment of the content
    sentiment = analyze_sentiment(content)

    # Send the result back to the client
    response = json.dumps({"sentiment": sentiment})
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8765, debug=True, threaded=True)
