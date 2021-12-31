from flask import request, jsonify
from app import app, accounts


@app.route('/')
@app.route('/index')
def index():
    return 'TEST SIMPLE API :: Calebe'



