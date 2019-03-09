from flask import Flask
app = Flask(__name__)


@app.route('/<name>')
def hello(name):
    return f"Hey there, {name}!"
