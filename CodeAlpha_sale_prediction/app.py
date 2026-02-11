from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# load trained model
model = joblib.load("sales_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        tv = float(request.form["tv"])
        radio = float(request.form["radio"])
        news = float(request.form["news"])

        prediction = model.predict([[tv, radio, news]])[0]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
