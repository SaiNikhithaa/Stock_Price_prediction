from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load("model/random_forest_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    open_price = float(request.form['open'])
    high_price = float(request.form['high'])
    low_price = float(request.form['low'])

    features = np.array([[open_price, high_price, low_price]])
    prediction = model.predict(features)[0]

    return render_template(
        'index.html',
        prediction_text=f"Predicted Closing Price: ₹{prediction:.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True)
