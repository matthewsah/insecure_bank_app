from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from authservice import AuthService
import re

auth_blueprint = Blueprint('auth', __name__)

authservice = AuthService()
    
@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            data = request.form

            # get data froms signup
            data1 = {
                'username': data['username'],
                'password': data['password'],
                'balance': data['balance']
            }

            # make sure signup username is valid
            pattern = r'[_\-\.0-9a-z]'
            if not re.match(pattern, data['username']):
                raise ValueError('Unable to sign up, please check input data.')
            
            pattern = r'(0|[1-9][0-9]*|[1-9][0-9]\.[0-9]{2})'
            if not re.match(pattern, str(data['balance'])):
                raise ValueError('Invalid balance, please check balance amount.')

            # register user
            authservice.register(data1['username'], data1['password'])

            # change to reroute to login page
            return redirect(url_for('auth.login'))
        except:
            return render_template('signup.html',
                                title="Sign Up", 
                                error="Unable to sign up, please check input data.")
    return render_template('signup.html')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form

        # get data from login form
        data1 = {
            'username': data['username'],
            'password': data['password']
        }

        # validate username
        pattern = r'[_\-\.0-9a-z]'
        if not re.match(pattern, data['username']):
            raise ValueError('Unable to sign up, please check input data.')
        
        authservice.login(data1['username'], data1['password'])

        # make sure only to go to index with session when user is logged in
        if 'username' in session:
            return redirect(url_for('index', session=session))
        else:
            return render_template('login.html')
    return render_template('login.html')

# do logout, build route to get accounts
@auth_blueprint.route('/logout', methods=["GET", "POST"])
def logout():
    if request.method == "POST":
        # delete critical user information from session once logged out
        session.pop('customer_id', None)
        session.pop('username', None)
        return redirect(url_for('index', session=session))
    return render_template('logout.html')
    