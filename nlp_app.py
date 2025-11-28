
# Streamlit Libraries
import streamlit as st

# NLP Libraries
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob
import re

####### PART 1 #######

# Create the GUI that takes user input for sentiment analysis. Provide a title, and define a text area (the input text can span multiple lines). Create a button "Analyze") that will then return the sentiment polarity and sentiment for the given text. [HINT: st.title(), st.subheader(), st.text_area(), st.button()]
st.title("NLP Sentiment Analyzer")
st.subheader("Enter text below to analyze its sentiment")
user_input = st.text_area("Enter your text here:")

if st.button("Analyze"):
    # start from the user’s input
    text = user_input

    # Keeping only Text and digits
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    # Removes Whitespaces
    text = re.sub(r"\'s", " ", text)
    # Removing Links if any
    text = re.sub(r"http\S+", " link ", text)
    # Removes Punctuations and Numbers
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)
    # Splitting Text
    text = text.split()
    # Lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
    text = " ".join(lemmatized_words)

    # Sentiment with TextBlob
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    result = sentiment_score 

    if result > 0:
        custom_emoji = ':blush:'
        st.success('Happy : {}'.format(custom_emoji))
    elif result < 0:
        custom_emoji = ':disappointed:'
        st.warning('Sad : {}'.format(custom_emoji))
    else:
        custom_emoji = ':confused:'
        st.info('Confused : {}'.format(custom_emoji))

    st.success("Polarity Score is: {}".format(result))
