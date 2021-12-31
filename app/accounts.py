from flask import abort


acc_dict = {}


def find_account(target):
    account = 0
    for p_id, p_info in acc_dict.items():
        for key in p_info:
            if key == 'id' and p_info[key] == target:
                account = p_id
    if account != 0:
        return account
    else:
        return '404'


def get_account_balance(acc_id):
    result = find_account(acc_id)

    if result != '404':
        return acc_dict[result]['balance']
    else:
        return abort(404)


def deposit(req_input):
    result = find_account(req_input['destination'])

    if result != '404':
        new_balance = acc_dict[result]['balance'] + req_input['amount']
        acc_dict[result]['balance'] = new_balance
        return {'destination': acc_dict[result]}
    else:
        new_id = len(acc_dict) + 1
        acc_dict[new_id] = {}
        acc_dict[new_id]['id'] = req_input['destination']
        acc_dict[new_id]['balance'] = req_input['amount']
        return {'destination': acc_dict[new_id]}


def withdraw(req_input):
    result = find_account(req_input['origin'])

    if result != '404':
        new_balance = acc_dict[result]['balance'] - req_input['amount']
        acc_dict[result]['balance'] = new_balance
        return {'origin': acc_dict[result]}
    else:
        return abort(404)


def transfer(req_input):
    return Merge(withdraw(req_input), deposit(req_input))


def Merge(dict1, dict2):
    res = dict1 | dict2
    return res
