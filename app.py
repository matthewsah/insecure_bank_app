from flask import Flask, render_template, session
from accountroutes import account_blueprint
from authroutes import auth_blueprint
import mariadb

app = Flask(__name__)

config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'flask_app',
    'raise_on_warnings': True
}

# not sure if this is actually needed anymore
def get_db_connection():
    """Establish and return a database connection."""
    try:
        conn = mariadb.connect(**config)
        print("Connection successful!")
        return conn
    except:
        print(f"Error connecting to MySQL")
        return None

@app.route('/')
def hello_world():
    return render_template('index.html', title="Homepage", session=session)

app.register_blueprint(account_blueprint)
app.register_blueprint(auth_blueprint)

app.run(host="0.0.0.0",port=8080,debug=True)
