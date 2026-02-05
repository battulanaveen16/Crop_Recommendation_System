import streamlit as st
import pandas as pd
import numpy as np
import requests
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# OpenWeather API settings
API_KEY = "2bc6e56e92b3253684420930d9eb188d"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather_data(city):
    params = {
        "q": city,
        "units": "metric",
        "appid": API_KEY
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        temps = []
        humidities = []
        rainfalls = []
        
        for entry in data["list"]:
            temps.append(entry["main"]["temp"])
            humidities.append(entry["main"]["humidity"])
            rainfalls.append(entry.get("rain", {}).get("3h", 0))
            
        return {
            "temperature": np.mean(temps),
            "humidity": np.mean(humidities),
            "rainfall": np.mean(rainfalls) * 3
        }
    except Exception as e:
        st.error(f"Weather API error: {str(e)}")
        return None

@st.cache_resource
def load_model():
    df = pd.read_csv("Updated_Crop_data.csv")
    df = df.dropna()
    
    le = LabelEncoder()
    df['Crop'] = le.fit_transform(df['Crop'])
    
    X = df[['Soil_pH', 'Nitrogen', 'Phosphorus', 'Potassium', 
            'Temperature', 'Humidity', 'Rainfall']]
    y = df['Crop']
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    return model, le

# Initialize session state
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

st.title("📥 Farm Input Details")

with st.form("input_form"):
    city = st.text_input("Enter your location (City, Country)", "New Delhi,IN")
    area = st.number_input("Land Area (acres)", 0.1, 1000.0, 1.0)
    soil_pH = st.slider("Soil pH", 5.0, 8.0, 6.5, 0.1)
    nitrogen = st.number_input("Nitrogen Level (kg/ha)", 0, 200, 50)
    phosphorus = st.number_input("Phosphorus Level (kg/ha)", 0, 200, 50)
    potassium = st.number_input("Potassium Level (kg/ha)", 0, 200, 50)
    
    submitted = st.form_submit_button("Get Recommendations")

if submitted:
    with st.spinner("Fetching weather data and analyzing..."):
        weather = get_weather_data(city)
        
        if weather:
            model, le = load_model()
            
            input_data = [[
                soil_pH, nitrogen, phosphorus, potassium,
                weather['temperature'], weather['humidity'], weather['rainfall']
            ]]
            
            probas = model.predict_proba(input_data)[0]
            top3_idx = np.argsort(probas)[-3:][::-1]
            top3_crops = le.inverse_transform(top3_idx)
            top3_probs = probas[top3_idx]
            
            st.session_state.recommendations = list(zip(top3_crops, top3_probs))
            st.session_state.weather_data = weather
            st.session_state.form_inputs = {
                'city': city,
                'area': area,
                'soil_pH': soil_pH,
                'nitrogen': nitrogen,
                'phosphorus': phosphorus,
                'potassium': potassium
            }
            st.session_state.form_submitted = True
            st.rerun()

if st.session_state.form_submitted:
    st.success("✅ Analysis complete! Please navigate to the Suggestions page using the sidebar.")
