import pandas
import streamlit as st
import send_email

st.header("Contact Me")
df = pandas.read_csv("topic_data.csv")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    options = st.selectbox(label="Select your topic!", options=df["topic"])
    raw_message = st.text_input("Your message")
    message = f"""\
Subject: New message from {user_email}
From: {user_email}
Topic: {options}
{raw_message}   
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email.send_email(message)
        st.info("Your message has been sent successfully.")