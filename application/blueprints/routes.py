# https://flask.palletsprojects.com/en/1.1.x/blueprints/#blueprints
from flask import Flask
from flask import Blueprint, render_template, abort

# Creates Route
route = Blueprint('route', __name__, template_folder='templates')

# Different endpoints
@route.route('/')
def home():
    return render_template('index.html')