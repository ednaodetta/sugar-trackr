from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('iri.pkl', 'rb'))

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
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    arr = np.array([[data1, data2, data3, data4]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)















