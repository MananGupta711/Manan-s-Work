import streamlit as st

st.title("Language Selector Box")

Languages = ["English", "Hindi", "Japanese", "French"]

selected_languages = st.selectbox("choose your languages : ", Languages)

st.write(f"You selected {selected_languages}")