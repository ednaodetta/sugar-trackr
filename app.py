from flask import Flask, render_template, request
import pickle
import numpy as np

# Load models and encoders
model = pickle.load(open('diabetes_model.pkl', 'rb'))
feature_order = pickle.load(open('feature_order.pkl', 'rb'))
gender_encoder = pickle.load(open('gender_encoder.pkl', 'rb'))
log_columns = pickle.load(open('log_columns.pkl', 'rb'))

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('html/form.html')

@app.route('/home')
def homee():
    return render_template('html/home.html')

@app.route('/result_diabetes')
def resultDiabetes():
    return render_template('html/result_diabetes.html')

@app.route('/result_nondiabetes')
def resultNonDiabetes():
    return render_template('html/result_nondiabetes.html')

@app.route('/artikel1')
def artikel1():
    return render_template('html/artikel1.html')

@app.route('/artikel2')
def artikel2():
    return render_template('html/artikel2.html') 

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    gender = request.form['gender']
    age = float(request.form['age'])
    hypertension = int(request.form['hypertension'])
    heart_disease = int(request.form['heart_disease'])
    bmi = float(request.form['bmi'])
    hba1c_level = float(request.form['HbA1c_level'])
    blood_glucose_level = float(request.form['blood_glucose_level'])

    # Encode gender correctly
    # gender = gender_encoder.transform([gender])[0]
    import pickle

# Load gender encoder
    with open('gender_encoder.pkl', 'rb') as f:
        gender_encoder = pickle.load(f)

# Ensure `gender_encoder` contains fitted classes
    if 'Male' not in gender_encoder.classes_ or 'Female' not in gender_encoder.classes_:
        gender_encoder.classes_ = np.array(['Female', 'Male'])  # Ensure correct classes

    # Now transform
    gender = gender_encoder.transform([gender])[0]


    # Create input dictionary
    input_data = {
        "gender": gender,
        "age": age,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "bmi": bmi,
        "HbA1c_level": hba1c_level,
        "blood_glucose_level": blood_glucose_level
    }

    # Apply log transformation
    for col in log_columns:
        input_data[col] = np.log1p(input_data[col])

    # Ensure feature order matches training
    features = np.array([[input_data[col] for col in feature_order]])

    # Make prediction
    pred = model.predict(features)
    print(f"Prediction Result: {pred}")  # Debugging

    # Redirect based on prediction
    if pred[0] == 1:
        return render_template('html/result_diabetes.html', data=pred)
    else:
        return render_template('html/result_nondiabetes.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)
