import streamlit as st
import requests

st.title("Imdad Sentiment Analysis App")
user_input = st.text_input("Enter your text:", "I love this product!")
if st.button("Analyze"):
    response = requests.post("http://127.0.0.1:5000/analyze", json={"text": user_input})
    if response.status_code == 200:
        result = response.json()
        st.success(f"Sentiment: {result['sentiment']}")
        st.info(f"Confidence: {result['confidence']:.2f}")
    else:
        st.error("Error: Could not connect to the API.")