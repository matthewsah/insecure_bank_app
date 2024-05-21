from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from authservice import AuthService

auth_blueprint = Blueprint('auth', __name__)

authservice = AuthService()
    
@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print('trying to post')
        try:
            data = request.form

            # print(data['account_name'])
            data1 = {
                'username': data['username'],
                'password': data['password']
            }

            print('received', data1)
            authservice.register(data1['username'], data1['password'])
            print('registered')
        
            # change to reroute to login page
            return redirect(url_for('auth.login'))
        except:
            print('why')
            print('exception caught')
            return render_template('signup.html',
                                title="Sign Up", 
                                error="Unable to sign up, please check input data.")
    print('GET')
    return render_template('signup.html')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form

        data1 = {
            'username': data['username'],
            'password': data['password']
        }

        print('received', data1)
        print(authservice.login(data1['username'], data1['password']))

        if 'username' in session:
            return redirect(url_for('index', session=session))
        else:
            return render_template('login.html')
    return render_template('login.html')