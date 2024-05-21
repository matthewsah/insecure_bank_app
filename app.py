from flask import Flask, render_template
from accountroutes import account_blueprint

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', title="Welcome", name="World")

app.register_blueprint(account_blueprint)

app.run(host="0.0.0.0",port=8080,debug=True)
