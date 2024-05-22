from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session, request
from accountservice import AccountService
import re

account_blueprint = Blueprint('account', __name__)

accservice = AccountService()
    
@account_blueprint.route('/account', methods=['GET', 'POST'])
def create_account():
    try:
        if request.method == 'POST':
            data = request.form

            # print(data['account_name'])
            data1 = {
                'customer_id': session['customer_id'],
                'account_name': data['account_name'],
                'balance':  data['balance'],
                'account_type': data['account_type']
            }
            pattern = r'(0|[1-9][0-9]*|[1-9][0-9]\.[0-9]{2})'
            if not re.match(pattern, str(data['balance'])):
                raise ValueError('Invalid balance, please check balance amount.')

            # print(data['customer_id'], data['account_name'], int(data['balance']), data['account_type'])
            accservice.createAccount(data1['customer_id'], data1['account_name'], float(data1['balance']), data1['account_type'])

            # go back to customer dashboard
            return redirect(url_for('index', session=session))
        else:
            return render_template('createaccount.html',
                                   title="Create an Account")
    except ValueError as e:
        return render_template('createaccount.html',
                               title="Create an Account", 
                               error=str(e))

@account_blueprint.route('/accounts', methods=['GET'])
def get_accounts():
    customer_id = session['customer_id']
    customer_result = accservice.getAccounts(customer_id)
    print(customer_result)
    return None

@account_blueprint.route('/account/<int:account_id>', methods=['GET'])
def account(account_id):
    try:
        if request.method == 'GET':
            acct = accservice.getAccountById(int(account_id))

            # TODO convert to html
            # return jsonify({'account_id': acct.account_id, 'account_name': acct.account_name, 'balance': acct.balance, 'account_type': acct.account_type})
            return render_template('updateaccount.html', 
                                   title="Update Account", 
                                   account_name=acct.account_name, 
                                   balance=acct.balance,
                                   error=request.args.get('error'))
    except Exception as e:
        return None

@account_blueprint.route('/account/<int:account_id>/withdraw', methods=['POST'])
def withdraw(account_id):
    try:
        if request.method == 'POST':
            acct = accservice.getAccountById(int(account_id))
            data = request.form
            data1 = {
                'change': float(data['change'])
            }

            pattern = r'(0|[1-9][0-9]*)(\.\d{1,2})?'
            if not re.match(pattern, str(data['change'])):
                raise ValueError('Invalid withdrawal amount')
            
            accservice.withdraw(int(account_id), data1['change'])

            return redirect(url_for('account.account', account_id=int(account_id)))
        else:
            return redirect(url_for('account.account', account_id=int(account_id)))
    except Exception as e:
        return redirect(url_for('account.account', account_id=int(account_id), error=str(e)))

@account_blueprint.route('/account/<int:account_id>/deposit', methods=['POST'])
def deposit(account_id):
    try:
        if request.method == 'POST':
            acct = accservice.getAccountById(int(account_id))
            data = request.form
            data1 = {
                'change': float(data['change'])
            }

            pattern = r'(0|[1-9][0-9]*)(\.\d{1,2})?'
            if not re.match(pattern, str(data['change'])):
                raise ValueError('Invalid deposit amount.')
            
            # TODO make withdraw return a snapshot of the account data
            accservice.deposit(int(account_id), data1['change'])

            return redirect(url_for('account.account', account_id=int(account_id)))
        else:
            return redirect(url_for('account.account', account_id=int(account_id)))
    except Exception as e:
        return redirect(url_for('account.account', account_id=int(account_id), error=str(e)))
