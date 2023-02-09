from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
model = pickle.load(open('random_forest_regression_model.pkl','rb'))

app = Flask(__name__, template_folder='Template', static_folder="static")
@app.route('/')
def index():
    return render_template('main.html')
@app.route('/predict', methods=['POST'])
def predict():
    Year = int(request.form.get('year'))
    Year = 2022-Year
    KM = int(request.form.get('kilometer'))
    Owner = request.form.get('owner')
    Mileage = float(request.form.get('mileage'))
    Engine = int(request.form.get('engine'))
    Power = float(request.form.get('power'))
    Location = request.form.get('location')
    Fuel= request.form.get('fuel')
    Transmission = request.form.get('transmission')

    arr1 = np.array([[Year, KM, Owner, Mileage, Engine, Power, Location,Fuel, Transmission]])
    prediction = model.predict(arr1)
    output = round(prediction[0], 2)
    if output < 0:
        return render_template('after.html', prediction_text="Sorry you cannot sell this car")
    else:
        return render_template('after.html', prediction_text="You Can Sell The Car at {} lakh".format(output))
if __name__=="__main__":
    app.run(debug=True)
