import streamlit as st

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