import sqlite3
from flask import Flask, jsonify, request
from methods import post_postcard

# create flask app
app = Flask(__name__)

@app.route('/postcards', methods=['POST'])
def postcards():
    data = request.form
    return(jsonify(data["year"]))


