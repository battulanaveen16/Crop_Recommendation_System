# 🌱 Climate Responsive Smart Farming

A smart farming assistant that provides personalized crop recommendations based on soil conditions, weather data, and location. The system also offers detailed budget estimations for selected crops to help farmers make informed decisions.

## Features

- 🌍 **Location-based Weather Analysis** using OpenWeather API
- 🌱 **Smart Crop Recommendations** powered by Machine Learning (Random Forest)
- 📊 **Top 3 Crop Suggestions** with suitability percentages
- 💰 **Detailed Budget Estimation** including costs, revenue, and profit projections
- 📱 **User-Friendly Interface** with multi-page navigation

## 🛠️ Technologies Used

- **Frontend**: Streamlit (Python)
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **Weather API**: OpenWeatherMap
- **Data Processing**: Pandas, NumPy

## 📸 Screenshots
###                                                         Home Page
![Homepage](https://github.com/Sanjai-K-learner/Crop-Recommendation-System/blob/main/pages/HomePage.PNG)
###                                                         Input Page
![Input Page](https://github.com/Sanjai-K-learner/Crop-Recommendation-System/blob/main/pages/InputPage.PNG)
###                                                         Suggestion Page
![Suggestion](https://github.com/Sanjai-K-learner/Crop-Recommendation-System/blob/main/pages/SuggestionPage.PNG)
###                                                         Budget Page
![Budget](https://github.com/Sanjai-K-learner/Crop-Recommendation-System/blob/main/pages/BudgetPage.PNG)

## 🏁 Getting Started

### 🔧 Requirements
- Python 3.8+
- Streamlit
- Required Python packages (install via requirements.txt)

### 🚀 Steps to Run the Project

1. **Clone the Repository**
   
2. **Install Dependencies**
    pip install -r requirements.txt
   
3. **Run the Application**
     streamlit run Home.py
   
4. **Access the Application**
    The application will automatically open in your default browser at           http://localhost:8501

### Project Structure

Crop Recommendation System/<br>
├── Home.py                 # Main application entry point<br>
├── 1_📥_Input.py           # Farm input data collection<br>
├── 2_🌱_Suggestions.py     # Crop recommendations display<br>
├── 3_💰_Budget.py          # Budget estimation<br>
├── Updated_Crop_data.csv   # Dataset for model training<br>
└── requirements.txt        # Python dependencies<br>


## 👨‍💻 Author
NAVEEN BATHULA - battulanaveen16@gmail.com
## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 💡 Future Improvements
- Expand crop database with more varieties  
- Add seasonal planting recommendations  
- Include pest/disease warnings  
- Multi-language support for regional farmers   
- Integration with soil testing APIs  
- Historical price trends for crops  
- Government subsidy information  
