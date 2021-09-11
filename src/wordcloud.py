import streamlit as st
import spacy
from utils.wordcloud_utils import plot_wordcloud, frequency_plot




def wordcloud_page():
    st.write('WordCloud Page')

    #Language
    langs = ['en', 'pt-br']
    language = st.radio("Select your Language", langs)
    if language == 'en':
        nlp = spacy.load("en_core_web_sm")
    else:
        st.write('Not supported yet :( Using english schema')
        nlp = spacy.load("en_core_web_sm")

    #Select Input type

    #Get text
    text_input = st.text_input("Insert your text here to generate a WordCloud!")



    #Generate WordCloud
    if st.button('Generate WordCloud'):
        if text_input:
            text = nlp(text_input)
            plot_wordcloud(text)

    #Generate other analysis with graphs
    n_terms_input = st.text_input('How many words to analyze')

    if st.button('Generate Other Graphs'):
        if n_terms_input and text_input:
            text_input = nlp(text_input)
            n_terms = int(n_terms_input)
            frequency_plot(text_input, n_terms)