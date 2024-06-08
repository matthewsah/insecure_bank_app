from accountroutes import account_blueprint
from authroutes import auth_blueprint
from accountservice import AccountService
from datetime import timedelta
from flask import Flask, jsonify, render_template, session
from flask_cors import CORS
import secrets


app = Flask(__name__)

# only allow the domain name that is valid to access account details
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

app.config['SECRET_KEY'] = secrets.token_urlsafe(16)

accservice = AccountService()

@app.before_request
def make_session_permanent():
    session.permanent = False
    app.permanent_session_lifetime = timedelta(minutes=5)

@app.after_request
def add_security_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'
    return response

@app.route('/')
def index():
    customer_data = None
    try:
        if app.config['SECRET_KEY'] != session.get('secret_key') and 'username' in session:
            session.pop('secret_key', None)
            session.pop('username', None)
            session.pop('customer_id', None)
        if 'username' in session:
            customer_data = accservice.getAccounts(session['customer_id'])
    except Exception as e:
        return jsonify({'error': 'Bad Request'}), 400
    return render_template('index.html', title="Homepage", session=session, customer=customer_data)

# Apply CORS to account blueprint
cors_account = CORS(account_blueprint, resources={r"/*": {"origins": "http://localhost:8080"}})

# Apply CORS to auth blueprint
cors_auth = CORS(auth_blueprint, resources={r"/*": {"origins": "http://localhost:8080"}})

app.register_blueprint(account_blueprint)
app.register_blueprint(auth_blueprint)

app.run(host="0.0.0.0",port=8080,debug=True)
