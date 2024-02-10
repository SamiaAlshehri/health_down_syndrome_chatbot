# app.py
import streamlit as st
from langchain_community.llms import Clarifai
import os

from dotenv import load_dotenv
load_dotenv()

# Set Clarifai PAT as environment variable
secret_key = os.getenv("SECRET_KEY")

if secret_key is not None:
    os.environ["CLARIFAI_PAT"] = secret_key
    st.write("CLARIFAI_PAT successfully set.")
else:
    st.write("SECRET_KEY is not set. Unable to set CLARIFAI_PAT.")

model_url_or_id = 'https://clarifai.com/openai/chat-completion/models/openai-gpt-4-vision'
clarifai_model = Clarifai(model_url=model_url_or_id)

def get_response(prompt):
    clarifai_response = clarifai_model.predict(prompt)
    return clarifai_response

def main():
    st.title("Yamani Toungo Chatbot")

    # Your Streamlit app logic goes here

    user_input = st.text_input("Enter your question:")
    yamani_toungo_prompt = st.checkbox("Talk with North Yemeni Toungo")

    if st.button("Get Response"):
        if yamani_toungo_prompt:
            # Set the prompt for North Yemeni Toungo
            prompt = "Generate a response in North Yemeni Toungo dialect: " + user_input

            # Use GPT-3.5 Turbo to generate the response
            bot_response = get_response(prompt)
        else:
            # Fallback to GPT model if question not found in the dataset
            bot_response = get_fallback_response(user_input)

        st.text("Bot Response:")
        st.write(bot_response)

if __name__ == '__main__':
    main()
