import streamlit as st
import requests
# from ..backend.app import predict_sentiment_all_emiten

def process_one(news : str):

    r = requests.post("http://127.0.0.1:8000/predict_sentiment_all_emiten/?news="+news)
    
    return r

def process_two(news : str, aspect : str):

    t = requests.post(f"http://127.0.0.1:8000/predict_sentiment_specific_emiten/?news={news}&aspect={aspect}")
    
    return t

# UI Layout

menu = ["1 Input","2 Input"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "1 Input":
    st.title("Sentiment Analysis")
    st.subheader("Sentiment analysis of Indonesian stock company articles with BERT")

    st.subheader("1 Input for Sentiment Analysis")
    with st.form(key='nlpForm'):
        news = st.text_area("Enter Article Here")
        submit_button = st.form_submit_button(label='Analyze')
        
        if submit_button:
            st.info("Results")
            predict = process_one(news)
            st.json(predict.text)
            
elif choice == "2 Input":
    st.title("Sentiment Analysis")
    st.subheader("Sentiment analysis of Indonesian stock company articles with BERT")
    
    st.subheader("2 Input for Sentiment Analysis")
    with st.form(key='nlpForm'):
        news = st.text_area("Enter Article Here")
        aspect = st.text_input("Enter Aspect Here")
        submit_button = st.form_submit_button(label='Analyze')
        
        if submit_button:
            st.info("Results")
            predict = process_two(news, aspect)
            st.json(predict.text)