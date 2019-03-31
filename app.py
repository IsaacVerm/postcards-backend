import sqlite3
from flask import Flask, jsonify, request, make_response
from db import *

# create flask app
app = Flask(__name__)


@app.route('/postcards', methods=['GET', 'POST'])
def postcards():
    # setup
    connection = create_postcards_connection()
    cursor = create_cursor(connection)
    create_cards_table(cursor)

    if request.method == 'POST':
        # save data to database
        data = request.form
        insert_values_into_cards_table(
            cursor, data['year'], data['description'], data['country'])
        save_data(connection)

        # return inserted data with status 201
        json_response = jsonify(year=data['year'],
                                description=data['description'],
                                country=data['country'])
        return make_response((json_response, 201))

    if request.method == 'GET':
        # get data from database
        cards = get_all_cards(cursor)

        # return to user
        return make_response((jsonify(cards), 200))

    # close connection
    close_connection(connection)
