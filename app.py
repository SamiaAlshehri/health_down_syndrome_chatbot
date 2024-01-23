# app.py
import streamlit as st
import pandas as pd
from langchain_community.llms import Clarifai
import os

# app.py
from flask import Flask, render_template, request, jsonify
import pandas as pd
from langchain_community.llms import Clarifai
import os
import streamlit as st

from dotenv import load_dotenv
load_dotenv()

# Set Clarifai PAT as environment variable
secret_key = os.getenv("SECRET_KEY")

if secret_key is not None:
    os.environ["CLARIFAI_PAT"] = secret_key
    st.write("CLARIFAI_PAT successfully set.")
else:
    st.write("SECRET_KEY is not set. Unable to set CLARIFAI_PAT.")

# Load CSV dataset
dataset = pd.read_csv('dataset/dataset.csv', encoding='latin1')
dataset['Question'] = dataset['Question'].fillna('')

model_url_or_id = 'https://clarifai.com/openai/chat-completion/models/openai-gpt-4-vision'
clarifai_model = Clarifai(model_url=model_url_or_id)

def get_response(user_input):
    clarifai_response = clarifai_model.predict(user_input)
    return clarifai_response

def get_fallback_response(user_input):
    # Fallback logic using GPT model
    return get_response(user_input)

def main():
    st.title("Down Syndrome Chatbot")

    # Your Streamlit app logic goes here

    user_input = st.text_input("Enter your question:")
    
    if st.button("Get Response"):
        matched_row = dataset[dataset['Question'].str.contains(user_input, case=False, na=False)]

        if not matched_row.empty:
            bot_response = matched_row.iloc[0]['Answer']
        else:
            # Fallback to GPT model if question not found in the dataset
            bot_response = get_fallback_response(user_input)

        st.text("Bot Response:")
        st.write(bot_response)

if __name__ == '__main__':
    main()
