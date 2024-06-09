from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session, request
from accountservice import AccountService
import re

account_blueprint = Blueprint('account', __name__)

accservice = AccountService()
    
@account_blueprint.route('/account', methods=['GET', 'POST'])
def create_account():
    try:
        if not 'username' in session:
            return redirect(url_for('index', session=session))

        if not any(domain in request.url for domain in ['localhost', '127.0.0.1']):
            return redirect(url_for('index', session=session))

        if request.method == 'POST':
            data = request.form

            # get data from form input
            data1 = {
                'customer_id': session['customer_id'],
                'account_name': data['account_name'],
                'balance':  data['balance'],
                'account_type': data['account_type']
            }

            # validate inputs
            pattern = r'(0|[1-9][0-9]*|[1-9][0-9]\.[0-9]{2})'
            if not re.match(pattern, str(data['balance'])):
                raise ValueError('Invalid balance, please check balance amount.')

            # insert account data into table
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

@account_blueprint.route('/account/<int:account_id>', methods=['GET'])
def account(account_id):
    try:
        if not 'username' in session:
            return redirect(url_for('index', session=session))
        
        if request.method == 'GET':
            # Get a single account
            acct = accservice.getAccountById(int(account_id))

            # Render the update account html page
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
        if not 'username' in session:
            return redirect(url_for('index', session=session))
        
        if request.method == 'POST':
            acct = accservice.getAccountById(int(account_id))
            data = request.form
            data1 = {
                'change': float(data['change'])
            }

            # verifying withdrawal amount
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
        if not 'username' in session:
            return redirect(url_for('index', session=session))

        if request.method == 'POST':
            acct = accservice.getAccountById(int(account_id))
            data = request.form
            data1 = {
                'change': float(data['change'])
            }

            # verifying deposity errors
            pattern = r'(0|[1-9][0-9]*)(\.\d{1,2})?'
            if not re.match(pattern, str(data['change'])):
                raise ValueError('Invalid deposit amount.')
            
            # use account service to deposit money
            accservice.deposit(int(account_id), data1['change'])

            return redirect(url_for('account.account', account_id=int(account_id)))
        else:
            return redirect(url_for('account.account', account_id=int(account_id)))
    except Exception as e:
        return redirect(url_for('account.account', account_id=int(account_id), error=str(e)))
