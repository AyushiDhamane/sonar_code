import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Streamlit Website", page_icon="🌟", layout="wide")

# Title and Welcome Message
st.title("Welcome to My Streamlit Website!")
st.write("This is a simple website built with Streamlit.")

# Add Name and Roll Number
name = st.text_input("Enter your name:")
roll_number = st.text_input("Enter your roll number:")

if name and roll_number:
    st.success(f"Hello, {name}! Your roll number is {roll_number}.")



# Content Based on Navigation Selection
if selected == "Home":
    st.header("Welcome to the Home Page")
    st.write("This is the home page of the website.")
elif selected == "About":
    st.header("About This Website")
    st.write("This is a basic Streamlit website with a navbar and styled elements.")
elif selected == "Contact":
    st.header("Contact Us")
    st.write("Feel free to reach out at `example@example.com`.")