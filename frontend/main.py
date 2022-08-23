import streamlit as st
from app import predict_sentiment
# from ../backend/app import predict_sentiment

# UI Layout
st.title("Sentiment Analysis")
st.subheader("Sentiment analysis of Indonesian stock company articles with BERT")

menu = ["Home","About"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
    st.subheader("Home")
    with st.form(key='nlpForm'):
        news_text = st.text_area("Enter Article Here")
        aspect_text = st.text_input("Enter Aspect Here")
        submit_button = st.form_submit_button(label='Analyze')
        
        if submit_button:
            predict = predict_sentiment(news_text, aspect_text)
            st.write(predict)

	# layout
    if submit_button:
        st.info("Results")