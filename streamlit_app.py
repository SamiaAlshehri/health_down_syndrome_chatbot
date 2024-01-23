# streamlit_app.py
import streamlit as st

def main():
    st.title("Streamlit Integration with Flask")

    user_input = st.text_input("Enter your question:")
    st.button("Submit")

    if st.button("Submit"):
        st.success(f"You submitted: {user_input}")

if __name__ == "__main__":
    main()
