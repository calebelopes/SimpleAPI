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


@app.route('/balance', methods=['GET'])
def balance():
    acc = request.args['id']
    return str(accounts.get_account_balance(acc))


@app.route('/event', methods=['POST'])
def event():
    input_req = request.get_json(force=True)

    if input_req['type'] == 'deposit':
        return jsonify(accounts.deposit(input_req))
    elif input_req['type'] == 'withdrawal':
        return jsonify(accounts.withdrawal(input_req))
    elif input_req['type'] == 'transfer':
        print()
    return 'OK'
