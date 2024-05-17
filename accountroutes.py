from flask import Blueprint, render_template, request, jsonify
from accountservice import AccountService

account_blueprint = Blueprint('account', __name__)

accservice = AccountService()
    
@account_blueprint.route('/account', methods=['GET', 'POST'])
def create_account():
    try:
        if request.method == 'POST':
            data = request.form

            # print(data['account_name'])
            data1 = {
                'customer_id': data['customer_id'],
                'account_name': data['account_name'],
                'balance':  data['balance'],
                'account_type': data['account_type']
            }

            # print(data['customer_id'], data['account_name'], int(data['balance']), data['account_type'])
            accservice.createAccount(data1['customer_id'], data1['account_name'], int(data1['balance']), data1['account_type'])

            # go back to customer dashboard
            return data1
        else:
            return render_template('createaccount.html', title="Create an Account")
    except Exception as e:
        return render_template('createaccount.html', title="Create an Account", error="Unable to create account, please check input data.")

@account_blueprint.route('/account/<int:account_id>', methods=['GET'])
def account(account_id):
    try:
        if request.method == 'GET':
            acct = accservice.getAccountById(int(account_id))

            # TODO convert to html
            return jsonify({'account_id': acct.account_id, 'account_name': acct.account_name, 'balance': acct.balance, 'account_type': acct.account_type})
    except Exception as e:
        return None