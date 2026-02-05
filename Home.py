import streamlit as st

st.set_page_config(
    page_title="AgriTech Advisor",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 AgriTech Crop Recommendation System")
st.markdown("""
### Welcome to the Smart Farming Assistant
Get personalized crop recommendations based on your soil conditions and location.
""")
st.sidebar.success("Navigate to the Input page using the sidebar to get started")
