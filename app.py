import sqlite3
from flask import Flask, jsonify, request
from methods import post_postcard

# create flask app
app = Flask(__name__)

# create postcards database
conn = sqlite3.connect('postcards.db')
c = conn.cursor()
c.execute('''CREATE TABLE cards
             (year text, description text, country text)''')


@app.route('/postcards', methods=['POST'])
def postcards():
    data = request.form
    return(jsonify(data["year"]))
