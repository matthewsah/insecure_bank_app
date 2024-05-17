from flask import Flask, render_template, session, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', title="Welcome", name="World")

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     # Assuming authentication is successful
#     session['username'] = username
#     return 'Logged in successfully!'

# @app.route('/profile')
# def profile():
#     if 'username' in session:
#         return 'Logged in as %s' % session['username']
#     return 'You are not logged in'

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return 'Logged out successfully'

app.run(host="0.0.0.0",port=8080,debug=True)
