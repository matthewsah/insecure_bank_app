from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', title="Welcome", name="World")

app.run(host="127.0.0.1",port=8080,debug=True)