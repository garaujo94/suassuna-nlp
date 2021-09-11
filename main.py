import streamlit as st
from utils.wordcloud_utils import plot_wordcloud
from src.wordcloud import wordcloud_page
import spacy

nlp = spacy.load("en_core_web_lg")
doc1 = nlp("I like salty fries and hamburgers hamburgers hamburgers.")


st.title('Suassuna NLP')

st.write('Future NLP system')

wordcloud_page()