import streamlit as st


st.set_page_config(page_title="World Cities", page_icon="🌍")

st.title("World Cities")
st.write("Welcome to the World Cities data app.")
st.write("Explore city populations, locations, and capital status on the app page.")

st.page_link("pages/app.py", label="Go to the app", icon="➡️")
