import json
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
import pickle as pk
from flask import Flask, request, Response, jsonify

app = Flask(__name__)

@app.route('/train', methods=['POST'])
def training():
    if request.method == "POST":
        try:
            dataset = pd.read_csv("./Advertising.csv", index_col=0)
            x = dataset.loc[:,"TV":"newspaper"]
            y = dataset['sales']
            model = LinearRegression()
            model.fit(x,y)
            fileName = "linearRegressionModel.model"
            pk.dump(model,open(fileName,'wb'))
            resp = {"status": "SUCCESS", "error": ""}
        except Exception as e:
            resp = {"status": "FAILURE", "error": str(e)}
        return jsonify(resp)


if __name__=='__main__':
    app.run(host="0.0.0.0",port=8000)
