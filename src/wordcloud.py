import streamlit as st
import spacy
from utils.wordcloud_utils import plot_wordcloud




def wordcloud_page():
    st.write('WordCloud Page')

    #Language
    langs = ['en', 'pt-br']
    language = st.radio("Select your Language", langs)
    if language == 'en':
        nlp = spacy.load("en_core_web_lg")
    else:
        st.write('Not supported yet :( Using english schema')
        nlp = spacy.load("en_core_web_lg")

    
    text_input = st.text_input("Insert your text here to generate a WordCloud!")
    if st.button('Generate WordCloud'):
        if text_input:
            text = nlp(text_input)
            plot_wordcloud(text)