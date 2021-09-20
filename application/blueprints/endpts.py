# https://flask.palletsprojects.com/en/1.1.x/blueprints/#blueprints
from flask import Flask
from flask import Blueprint, render_template, abort
import json

from application.middleware.extensions import mongo

# Creates Route
endpt = Blueprint('endpt', __name__)

# Different endpoints
@endpt.route('/')
def home():
    return render_template('index.html')

@endpt.route('/test')
def test():
    try:
        return json.dumps({
            'payload': 'working',
            'status': 200
        })
    except:
        return json.dumps({
            'payload': 'yikes',
            'status': 400
        })

@endpt.route('/test/insert', methods=['GET', 'POST'])
def test_insert():
    try:
        if mongo.check_connection == False:
            mongo.make_connection()

        payload = {
            'data': 'test insertion'
        }
        test = mongo.insert('test', payload)

        print(test)

        if test == None:
            return json.dumps({
                'payload': 'Error Occured while inserting',
                'status': 400
            })

        return json.dumps({
            'payload': 'Successfully inserted entry',
            'status': 200
        })
    except Exception as err:
        return json.dumps({
            'payload': err,
            'status': 200
        })
