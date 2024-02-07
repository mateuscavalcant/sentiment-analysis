from textblob import TextBlob

def analyze_sentiment(text):
    """
    Function to analyze the sentiment of a text.
    Returns a tuple containing the sentiment label.
    Sentiment label can be Positive, Negative, or Neutral.
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        sentiment_label = "Positive"
    elif sentiment < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    return sentiment_label
