from textblob import TextBlob

def sentiment_analyzer(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    print("Sentiment:", sentiment_analyzer(user_input))
