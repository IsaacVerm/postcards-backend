import sqlite3
from flask import Flask, jsonify, request, make_response
from db import *

# create flask app
app = Flask(__name__)


@app.route('/postcard', methods=['POST'])
def postcard():
    # setup
    connection = create_postcards_connection()
    cursor = create_cursor(connection)
    create_cards_table(cursor)

    # save data to database
    data = request.form
    insert_card_into_cards_table(
        cursor, data['cardId'], data['photoUrl'], data['name'], data['description'], data['creationDate'])
    save_data(connection)

    # response
    response = make_response('', 201)
    response.headers['Location'] = f"/postcard/{data['cardId']}"
    return response


@app.route('/postcard/<cardId>', methods=['GET', 'DELETE'])
def postcard_cardid(cardId):
    # setup
    connection = create_postcards_connection()
    cursor = create_cursor(connection)

    if request.method == 'DELETE':
        # delete card with cardId in db
        delete_card_from_cards_table(cursor, connection, cardId)

        # confirm succesful removal of resource by returning 204
        return make_response('', 204)

    if request.method == 'GET':
        # find card with cardId in db
        card = find_card_in_cards_table(cursor, cardId)

        # return the card found and return 200 if a card exists
        if card is not None:
            return make_response(jsonify(dict(card)), 200)

        # return an empty body and status 204 if no card exists
        if card is None:
            return make_response('', 204)


@app.route('/postcards')
def postcards():
    # setup
    connection = create_postcards_connection()
    cursor = create_cursor(connection)

    # get cards from database
    cards = get_all_cards(cursor)

    # make cards json serializable as list of dictionaries
    cards_list = []
    for card in cards:
        cards_list.append(dict(card))

    # return the cards found and 200 if there is at least one card
    if len(cards_list) > 0:
        return make_response(jsonify({'cards': cards_list}), 200)

    # return 204 if no cards were found
    if len(cards_list) == 0:
        return make_response('', 200)
