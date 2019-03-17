from flask import Flask, render_template
from models import credentials

app = Flask(__name__)


@app.route('/credentials/view/<name>')
def view_credentials(name):
    return render_template('hello.html', name=name)

@app.route('/credentials/<name>')
def get_credentials(name):
    return credentials(name)
