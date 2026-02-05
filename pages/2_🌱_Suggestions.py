import streamlit as st

st.title("🌱 Crop Recommendations")

if 'form_submitted' not in st.session_state or not st.session_state.form_submitted:
    st.warning("Please submit your farm details on the Input page first")
    st.stop()

if 'recommendations' not in st.session_state:
    st.error("No recommendations found. Please go back to Input page")
    st.stop()

# Display farm summary
weather = st.session_state.weather_data
form_inputs = st.session_state.form_inputs

st.subheader("Farm Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Location", form_inputs['city'])
col2.metric("Land Area", f"{form_inputs['area']} acres")
col3.metric("Soil pH", form_inputs['soil_pH'])

st.divider()
st.subheader("Recommended Crops")

for i, (crop, prob) in enumerate(st.session_state.recommendations, 1):
    with st.container():
        col1, col2 = st.columns([3, 1])
        col1.subheader(f"{i}. {crop}")
        col1.write(f"Suitability: {prob*100:.1f}%")
        col1.write(f"Temperature: {weather['temperature']:.1f}°C")
        col1.write(f"Humidity: {weather['humidity']:.1f}%")
        
        if col2.button(f"Estimate Budget for {crop}", key=f"budget_{i}"):
            st.session_state.selected_crop = crop
            st.switch_page("pages/3_💰_Budget.py")
