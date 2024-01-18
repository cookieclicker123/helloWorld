import nltk

# Check if the vader_lexicon is already downloaded, download if not
try:
    # This line checks if the lexicon is available
    nltk.data.find('sentiment/vader_lexicon.zip/vader_lexicon/vader_lexicon.txt')
except LookupError:
    # If not, it downloads the lexicon
    nltk.download('vader_lexicon')