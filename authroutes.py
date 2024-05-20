from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from authservice import AuthService

auth_blueprint = Blueprint('auth', __name__)

authservice = AuthService()
    
@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    try:
        if request.method == 'POST':
            print('trying to post')
            data = request.form

            # print(data['account_name'])
            data1 = {
                'username': data['username'],
                'password': data['password']
            }

            print('received', data1)
            authservice.register(data1['username'], data1['account_name'], data1['password'])
        
            # change to reroute to login page
            return data1
        else:
            return render_template('signup.html',
                                   title="Login")
    except Exception as e:
        print('exception caught')
        return render_template('createuser.html',
                               title="Sign Up", 
                               error="Unable to sign up, please check input data.")