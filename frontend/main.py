import streamlit as st
import requests

def process_one(news):
    r = requests.post(f"http://127.0.0.1:8000/predict_sentiment_all_emiten/?news={news}")
    return r

def process_two(news, aspect):
    t = requests.post(f"http://127.0.0.1:8000/predict_sentiment_specific_emiten?news={news}&aspect={aspect}")
    return t

# UI Layout
menu = ["1 Input","2 Input"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "1 Input":
    st.title("Sentiment Analysis")
    st.subheader("Sentiment analysis of Indonesian stock company articles with BERT")

    st.subheader("1 Input for Sentiment Analysis")
    with st.form(key='nlpForm'):
        news = st.text_area("Enter Article Here", height=200)
        submit_button = st.form_submit_button(label='Analyze')
        if submit_button:
            st.info("Results")
            try:
                predict = process_one(news)
                st.json(predict.text)
            except:
                st.write("""
                         ## SYSTEM ERROR
                         - Check FastAPI connection
                         - Check the input entered""")
                
elif choice == "2 Input":
    st.title("Sentiment Analysis")
    st.subheader("Sentiment analysis of Indonesian stock company articles with BERT")
    
    st.subheader("2 Input for Sentiment Analysis")
    with st.form(key='nlpForm'):
        news = st.text_area("Enter Article Here", height=200)
        aspect = st.text_input("Enter Aspect Here")
        submit_button = st.form_submit_button(label='Analyze')
        if submit_button:
            st.info("Results")
            try:
                predict = process_two(news, aspect)
                st.json(predict.text)
            except:
                st.write("""
                         ## SYSTEM ERROR
                         - Check FastAPI connection
                         - Check the input entered""")