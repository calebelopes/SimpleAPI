from flask import request, jsonify, make_response
from app import app, accounts


@app.route('/')
@app.route('/index')
def index():
    return 'TEST SIMPLE API :: Calebe'


@app.route('/reset', methods=['POST'])
def reset():
    accounts.acc_dict = {}
    return 'OK'


@app.route('/balance', methods=['GET'])
def balance():
    acc = request.args['account_id']
    return str(accounts.get_account_balance(acc))


@app.route('/event', methods=['POST'])
def event():
    input_req = request.get_json(force=True)

    if input_req['type'] == 'deposit':
        return jsonify(accounts.deposit(input_req)), 201
    elif input_req['type'] == 'withdraw':
        return jsonify(accounts.withdraw(input_req)), 201
    elif input_req['type'] == 'transfer':
        return jsonify(accounts.transfer(input_req)), 201
    else:
        return 'Wrong parameter type'


@app.errorhandler(404)
def not_found(error):
    print(error)
    return '0', 404
