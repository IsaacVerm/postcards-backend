from flask import Flask, jsonify, render_template
app = Flask(__name__)


@app.route('/credentials/view/<name>')
def view_credentials(name):
    return render_template('hello.html', name=name)


@app.route('/credentials/<name>')
def credentials(name):
    if name == "me":
        return jsonify(user='myself', password='sense')
    if name == "you":
        return jsonify(user='yourself', password='nonsense')
    else:
        return ''
