from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/<name>')
def credentials(name):
    if name == "me":
        return jsonify(user='myself', password='sense')
    if name == "you":
        return jsonify(user='yourself', password='nonsense')
