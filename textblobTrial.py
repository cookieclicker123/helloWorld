from textblob import TextBlob   

def analyze_mood(user_input):
    analysis = TextBlob(user_input)
    
    # Analyze sentiment polarity
    if analysis.sentiment.polarity > 0:
        return 'You seem to be in a positive mood!'
    elif analysis.sentiment.polarity < 0:
        return 'It sounds like you might be feeling a bit negative.'
    else:
        return 'Your mood appears to be neutral.'

# Take input from the user
user_feeling = input("How are you feeling today? ")
count = 0
for i in user_feeling:
    if i == "e":
        count+=1

print("There were {} e's in your sentence".format(count))

# Analyze and print the result
result = analyze_mood(user_feeling)
print(result)