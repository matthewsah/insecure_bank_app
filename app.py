from flask import Flask, render_template, session
from accountroutes import account_blueprint
from authroutes import auth_blueprint
import mariadb

app = Flask(__name__)
app.config['SECRET_KEY'] = 'x162klqzp23p01nIug'

@app.route('/')
def hello_world():
    return render_template('index.html', title="Homepage", session=session)

app.register_blueprint(account_blueprint)
app.register_blueprint(auth_blueprint)

app.run(host="0.0.0.0",port=8080,debug=True)
