import streamlit as st
import numpy as np
import joblib

model = joblib.load("iris_model.pkl")

st.title("🌸 Iris Flower Classification")
st.write("Enter flower measurements to predict the species")

# ---- Inputs (EMPTY by default) ----
sepal_length = st.text_input("Sepal Length (cm)", placeholder="Enter value (4.0cm – 8.0cm)")


sepal_width = st.text_input("Sepal Width (cm)", placeholder="Enter value (2.0cm – 4.5cm)")


petal_length = st.text_input("Petal Length (cm)", placeholder="Enter value (1.0cm – 7.0cm)")


petal_width = st.text_input("Petal Width (cm)", placeholder="Enter value (0.1cm – 2.5cm)")


# ---- Predict button ----
if st.button("Predict"):
    try:
        sl = float(sepal_length)
        sw = float(sepal_width)
        pl = float(petal_length)
        pw = float(petal_width)

        # range validation
        if not (4.0 <= sl <= 8.0 and 2.0 <= sw <= 4.5 and
                1.0 <= pl <= 7.0 and 0.1 <= pw <= 2.5):
            st.error("❌ Please enter values within the recommended ranges.")
        else:
            features = np.array([[sl, sw, pl, pw]])
            prediction = model.predict(features)[0]
            st.success(f"🌼 Predicted Species: {prediction}")

    except ValueError:
        st.error("❌ Please enter valid numeric values.")
