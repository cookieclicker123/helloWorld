#Create a sentiment analysis tool that analyzes text data (like tweets, reviews, or articles) to determine the sentiment 
#(positive, negative, neutral). You can use natural language processing libraries like NLTK or spaCy.

#Importing the libraries

# Importing the libraries
import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the vader_lexicon package


# Initialize the VADER sentiment intensity analyzer
sia = SentimentIntensityAnalyzer()

# Analyze the sentiment of a text
def analyze_sentiment(text):
    # Get the sentiment scores dictionary
    sentiment_scores = sia.polarity_scores(text)

    # Get the sentiment from the scores
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment

# Test the function
text = "I love this product! It's awesome."
print(analyze_sentiment(text))  # Output: Positive

