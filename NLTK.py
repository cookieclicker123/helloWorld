import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


# Download VADER lexicon
nltk.download('vader_lexicon')

def analyze_mood(user_input):
    sia = SentimentIntensityAnalyzer()
    
    # Analyze sentiment with VADER
    sentiment_score = sia.polarity_scores(user_input)['compound']
    
    if sentiment_score >= 0.05:
        return 'You seem to be in a positive mood!'
    elif sentiment_score <= -0.05:
        return 'It sounds like you might be feeling a bit negative.'
    else:
        return 'Your mood appears to be neutral.'

# Take input from the user
user_feeling = input("How are you feeling today? ")

# Analyze and print the result
result = analyze_mood(user_feeling)
print(result)