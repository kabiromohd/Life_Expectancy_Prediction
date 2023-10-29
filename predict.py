import pickle
import numpy as np

from flask import Flask
from flask import request
from flask import jsonify

input_file = "model_rf_1.pkl"
input_file2 = "model_dv.pkl"

with open(input_file, 'rb') as f_in: 
    model = pickle.load(f_in)
    
with open(input_file2, 'rb') as f_in2: 
    dv = pickle.load(f_in2)
    
app = Flask('life_expectancy')

@app.route('/predict', methods = ['POST'])
def predict():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict(X)
    life_expectancy = np.expm1(y_pred)

    result = {
        'Predicted Life Expectancy': float(life_expectancy)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 9690)