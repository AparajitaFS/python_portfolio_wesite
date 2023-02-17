import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/15.png")

with col2:
    st.title("Aparajita Pandey")
    content = """Hi, I am Aparajita! I am a Software Engineer, Youtuber, Blogger." \
              I am post graduated in 2018 with computer application
              """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python.
"""

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])