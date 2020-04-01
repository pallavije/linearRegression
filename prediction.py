import json
import pickle as pk
from flask import Flask, request, Response, jsonify

app = Flask(__name__)
fileName = "linearRegressionModel.model"
model = pk.load(open(fileName,'rb'))

@app.route('/predict', methods=['GET'])
def prediction():
    if request.method == "GET":
        #data = request.get_json()
        #query = data['inputs']
        tv = int(request.args['tv'])
        radio = int(request.args.get('radio'))
        newspaper = int(request.args.get('newspaper'))
        query = [tv,radio,newspaper]
        print(query)
        try:
            prediction = model.predict([query])
            print(prediction)
            resp = {"status": "SUCCESS", "error": "", "sales": prediction[0]}
        except Exception as e:
            resp = {"status": "FAILURE", "error": str(e), "sales": ""}
        return jsonify(resp)


if __name__=='__main__':
    app.run(host="0.0.0.0",port=8080)

