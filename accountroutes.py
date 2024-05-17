from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from accountservice import AccountService

account_blueprint = Blueprint('account', __name__)

accservice = AccountService()

@account_blueprint.route('/account', methods=['GET', 'POST'])
def create_account():
    try:
        if request.method == 'POST':
            data = request.form
            data = jsonify(data)
        else:
            return render_template('createaccount.html', title="Create an Account")
    except Exception as e:
        return render_template('createaccount.html', title="Create an Account", error="Unable to create account, please check input data.")
    
