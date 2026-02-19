🚗 Car Price Prediction using Machine Learning
📌 Project Overview

This project predicts the selling price of a used car based on user inputs using Machine Learning.
It includes a trained Linear Regression model and an interactive Streamlit web application for real-time predictions.

🎯 Features

Data preprocessing and feature engineering

One-hot encoding for categorical variables

Linear Regression model training

Model and feature saving using joblib

Interactive Streamlit UI

Real-time price prediction in lakhs 💰

🧠 Tech Stack

Python

Pandas

NumPy

Scikit-learn

Streamlit

Joblib

⚙️ How It Works

User enters car details:

Year

Present Price

Kilometers Driven

Fuel Type

Seller Type

Transmission

Owner Count

The app processes inputs to match training features.

The trained Linear Regression model predicts the estimated selling price.

📂 Project Structure
├── car_price_model.pkl
├── car_features.pkl
├── app.py
├── dataset.csv
└── README.md

🚀 Installation & Run
1️⃣ Clone the repository
git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run Streamlit app
streamlit run app.py

📸 Output

The system returns:

✅ Predicted selling price in lakhs based on user input.

📈 Future Improvements

Try advanced models (Random Forest, XGBoost)

Improve UI design

Deploy on cloud (Streamlit Cloud / Render)

Add model accuracy metrics in UI

🙌 Author

Ishwari More
