import joblib
import pandas as pd
import numpy as np

from flask import Flask, request, jsonify

app = Flask(__name__)

data = pd.read_csv("dataset.csv")
model = joblib.load('model.joblib')

def encodeIp(ipData):
    encodedIp = []
    if ipData[0]=="sunny":
        encodedIp.append(1)
    elif ipData[0]=="rainy":
        encodedIp.append(2)

    if ipData[1]=="sandy":
        encodedIp.append(1)
    elif ipData[1]=="loam":
        encodedIp.append(2)
    elif ipData[1]=="clay":
        encodedIp.append(3)

    if ipData[2]=="basmathi":
        encodedIp.append(1)
    elif ipData[2]=="japonica":
        encodedIp.append(2)
    elif ipData[2]=="indica":
        encodedIp.append(3)
    elif ipData[2]=="durum":
        encodedIp.append(4)    
    elif ipData[2]=="bread":
        encodedIp.append(5)    

    encodedIp.append(int(ipData[3]))
    encodedIp.append(1)

    if ipData[5]=="wind":
        encodedIp.append(1)
    elif ipData[5]=="sunlight":
        encodedIp.append(2)
    elif ipData[5]=="humidity":
        encodedIp.append(3)

    return encodedIp

@app.route('/predict', methods=['POST'])
def predict():
    request_data = request.json  # Assuming the input data is sent as JSON
    ipData = request_data['data']  # Assuming the input data array is stored in 'data' key
    ipData=['sunny','loam','basmathi','54','flood','wind']
    encoded_ip_data = encodeIp(ipData)  # Encode the input data
    prediction = model.predict(np.array(encoded_ip_data).reshape(1, -1))  # Make prediction
    return jsonify({'prediction': prediction.tolist()})

@app.route('/')
def home():
    return 'Welcome to the API'

if __name__ == '__main__':
    app.run(debug=False)

