from app import  app
from flask import request, make_response
from flask import jsonify


@app.route('/')
def index():
    return jsonify({"name": "123", "sex": 1, "age": 25})


@app.route('/user')
def user():
    resp = make_response()
    resp.headers['test'] = 'test'
    name = request.values.get('name')
    resp.data = name
    return resp
