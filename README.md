
# Titanic Passenger Survival Prediction

This project is a machine learning web application that predicts whether a passenger survived the Titanic disaster based on various input features.

## Features
- Built using Flask for the backend
- Uses a pre-trained machine learning model (`Titanic.pkl`) for predictions
- Accepts user input via a web form
- Displays survival prediction based on input data

## Files Overview
- `app.py` - The Flask application that serves the web interface and makes predictions.
- `Titanic.pkl` - A trained machine learning model used for prediction.
- `cleaned_titanic_dataset.csv` - The cleaned dataset used for training the model.
- `Titanic data cleaning & EDA.ipynb` - Jupyter notebook for data cleaning and exploratory data analysis (EDA).
- `Titanic Model training.ipynb` - Jupyter notebook for model training.
- `templates/index.html` - The HTML template for the web interface.

## Installation & Usage
1. Install dependencies:
   ```bash
   pip install flask pandas pickle5
2. Run the Flask app:
   ```bash
   python app.py

Open http://127.0.0.1:5000/ in your browser and enter passenger details to get a prediction.
