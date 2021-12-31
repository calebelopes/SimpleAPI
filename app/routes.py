from flask import request, jsonify
from app import app, accounts


@app.route('/')
@app.route('/index')
def index():
    return 'TEST SIMPLE API :: Calebe'


@app.route('/reset', methods=['POST'])
def reset():
    accounts.acc_dict = {}
    return 'Values have been reset'
