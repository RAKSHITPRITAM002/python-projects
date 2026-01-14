import streamlit as st

st.title('My First Streamlit App in VS Code')
st.write('Hello, world! This app is running from VS Code.')


user_name = st.text_input("What's your name?")
if user_name:
    st.write(f'Welcome, {user_name}!')
