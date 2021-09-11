import spacy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import streamlit as st

def count_words(spacy_text):
    words = [token.text
         for token in spacy_text
         if not token.is_stop and not token.is_punct]
    
    words_frequency = Counter(words)

    return words, words_frequency

def plot_wordcloud(spacy_text):

    _, words_frequency = count_words(spacy_text)

    #plt.figure(figsize = (20,20))
    fig, ax = plt.subplots()
    wc = WordCloud(max_words = 2000 , width = 1600 , height = 800).fit_words(words_frequency)
    ax.imshow(wc , interpolation = 'bilinear')
    st.pyplot(fig)

def frequency_plot(spacy_text, n_terms):
    _, words_frequency = count_words(spacy_text)
    
    words_frequency = list(zip(words_frequency.values(), words_frequency.keys()))
    words_frequency = sorted(words_frequency, reverse=True)
    words_frequency = dict(words_frequency)

    fig, ax = plt.subplots()
    sns.barplot(x=list(words_frequency.keys())[:n_terms],y=list(words_frequency.values())[:n_terms])
    #ax.imshow(wc)
    st.pyplot(fig)