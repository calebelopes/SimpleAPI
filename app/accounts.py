acc_dict = {
    1: {'id': '100', 'balance': '1200'},
    2: {'id': '200', 'balance': '1200'},
    3: {'id': '300', 'balance': '1200'}
}


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
        return 'ID NOT FOUND'


def deposit(req_input):
    result = find_account(req_input['destination'])

    if result != '404':
        new_balance = acc_dict[result]['balance'] + req_input['amount']
        acc_dict[result]['balance'] = new_balance
        return acc_dict[result]
    else:
        new_id = len(acc_dict) + 1
        acc_dict[new_id] = {}
        acc_dict[new_id]['id'] = req_input['destination']
        acc_dict[new_id]['balance'] = req_input['amount']
        print(acc_dict)
        return acc_dict[new_id]
