import spacy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import streamlit as st

def plot_wordcloud(spacy_text):

    words = [token.text
         for token in spacy_text
         if not token.is_stop and not token.is_punct]
    
    words_frequency = Counter(words)

    #plt.figure(figsize = (20,20))
    fig, ax = plt.subplots()
    wc = WordCloud(max_words = 2000 , width = 1600 , height = 800).fit_words(words_frequency)
    ax.imshow(wc , interpolation = 'bilinear')
    st.pyplot(fig)