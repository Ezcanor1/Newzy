import streamlit as st
import nltk
from textblob import TextBlob
from newspaper import Article

# Download the 'punkt' package for sentence tokenization
nltk.download('punkt')

# URL of the article
url = 'https://indianexpress.com/section/india/'

# Create an Article object
article = Article(url)

# Download and parse the article
article.download()
article.parse()

# Perform NLP (Natural Language Processing) on the article
article.nlp()

# Display the extracted information using Streamlit
st.title("Article Information")

st.subheader("Title")
st.write(article.title)

st.subheader("Authors")
st.write(", ".join(article.authors) if article.authors else "N/A")

st.subheader("Publish Date")
st.write(article.publish_date if article.publish_date else "N/A")

st.subheader("Summary")
st.write(article.summary)

