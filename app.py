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

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response_route():
    user_input = request.form['user_input']
    matched_row = dataset[dataset['Question'].str.contains(user_input, case=False, na=False)]

    if not matched_row.empty:
        bot_response = matched_row.iloc[0]['Answer']
    else:
        # Fallback to GPT model if question not found in the dataset
        bot_response = get_fallback_response(user_input)

    return jsonify({'response': bot_response})

def main():
    st.set_page_config(page_title="Streamlit and Flask Chat App", page_icon=":robot_face:")
    st.title("Chat With Us")

    # Streamlit components
    user_input = st.text_input("Type your message...")

    if st.button("Send"):
        if user_input.strip():
            # Fetch bot response from Flask server
            bot_response = fetch_bot_response(user_input)
            st.write(f"**You:** {user_input}")
            st.write(f"**Chatbot:** {bot_response}")

def fetch_bot_response(user_input):
    response = requests.post('http://127.0.0.1:5000/get_response', data={'user_input': user_input})
    return response.json()['response']

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
    main()
