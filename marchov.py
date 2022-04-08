import markovify
import streamlit
file= open('news.txt', 'r', encoding='utf-8').read()

text_model = markovify.NewlineText(file, state_size = 1, well_formed=False)

text= text_model.make_sentence()

streamlit.write(text)