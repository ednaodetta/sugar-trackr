from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('diabetes_model.pkl', 'rb'))

app = Flask(__name__)



@app.route('/form')
def form():
    return render_template('html/form.html')

@app.route('/result_diabetes')
def result_diabetes():
    return render_template('html/result_diabetes.html')

@app.route('/result_nondiabetes')
def result_nondiabetes():
    return render_template('html/result_nondiabetes.html')

@app.route('/home')
def Home():
    return render_template('html/home.html')

@app.route('/artikel1')
def artikel1():
    return render_template('html/artikel1.html')


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

    # Encode gender (Male = 1, Female = 0)
    gender = 1 if gender.lower() == "male" else 0

    # Create feature array
    # features = np.array([[gender, age, hypertension, heart_disease, bmi, hba1c_level, blood_glucose_level]])
    features = np.array([[gender, age, hypertension, heart_disease, bmi, hba1c_level, blood_glucose_level]])

    # Make prediction
    pred = model.predict(features)

    # Redirect based on prediction
    if pred[0] == 1:
        return render_template('html/result_diabetes.html', data=pred)
    else:
        return render_template('html/result_nondiabetes.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)