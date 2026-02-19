# 📊 Sales Prediction System

A machine learning web application that predicts **sales based on advertising budgets** across TV, Radio, and Newspaper channels.

This project demonstrates an end-to-end ML workflow — from data preprocessing to model deployment using Flask.

---

## 🚀 Project Overview

Businesses invest heavily in advertising but often lack clear insight into which channel drives sales the most.

This system:
- Takes advertising budgets as input  
- Uses a trained Linear Regression model  
- Predicts expected sales in real time  
- Provides an interactive web interface  

---

## 🧠 Machine Learning Details

- **Algorithm:** Linear Regression  
- **Features:**
  - TV Advertising Budget  
  - Radio Advertising Budget  
  - Newspaper Advertising Budget  
- **Target:** Sales  
- **Evaluation Metric:** R² Score  

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Flask  
- Joblib  
- HTML, CSS  
- Jinja2  

---

## 📂 Project Structure

CodeAlpha_sales_prediction/
│
├── app.py
├── sales_model.pkl
│
├── templates/
│ └── index.html
│
├── static/
│ ├── style.css
│ └── sales.jfif
│
└── README.md


---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository

git clone <repository-url>
cd CodeAlpha_sales_prediction
2️⃣ Install dependencies
pip install flask scikit-learn joblib numpy pandas
3️⃣ Run the Flask app
python app.py
4️⃣ Open in browser
http://127.0.0.1:5000
🧾 Input Ranges
Feature	Range
TV	0 – 300
Radio	0 – 50
Newspaper	0 – 100
These limits match the training data distribution.

✨ Features
Interactive web interface

Real-time sales prediction

Input validation with ranges

Values persist after prediction

Reset functionality

Clean responsive UI

Flask backend integration

📈 Key Insights
Radio advertising shows the strongest impact on sales

TV advertising significantly contributes to sales

Newspaper advertising has minimal influence

🧪 Sample Output
Predicted Sales: 15.42
🗣️ Viva / Interview Summary
This project uses a Linear Regression model to predict sales from advertising budgets and deploys it using Flask with a dynamic HTML/CSS frontend powered by Jinja.

🔮 Future Improvements
Add visual analytics dashboard

Try advanced regression models

Deploy to cloud (Render / AWS)

Improve UI with Bootstrap
