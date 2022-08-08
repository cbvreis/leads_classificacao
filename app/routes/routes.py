from app import app
from flask import jsonify, request
from ..views import pipeline

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello World!'})


@app.route('/predict', methods=['GET'])
def predict_data():
    return pipeline.predict_all()
