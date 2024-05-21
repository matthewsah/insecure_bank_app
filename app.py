from flask import Flask, render_template, session
from accountroutes import account_blueprint
from authroutes import auth_blueprint
from accountservice import AccountService

app = Flask(__name__)
app.config['SECRET_KEY'] = 'x162klqzp23p01nIug'

accservice = AccountService()

@app.route('/')
def index():
    customer_data = None
    try:
        if 'username' in session:
            customer_data = accservice.getAccounts(session['customer_id'])
    except Exception as e:
        print(e)
    return render_template('index.html', title="Homepage", session=session, customer=customer_data)

app.register_blueprint(account_blueprint)
app.register_blueprint(auth_blueprint)

app.run(host="0.0.0.0",port=8080,debug=True)
