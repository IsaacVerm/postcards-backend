import sqlite3
from flask import jsonify


def save_data(connection):
    connection.commit()


def create_postcards_connection():
    connection = sqlite3.connect('postcards.db')
    connection.row_factory = sqlite3.Row
    return connection


def create_cursor(connection):
    cursor = connection.cursor()
    return cursor


def create_cards_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS cards
             (cardId text, photoUrl text, name text, description text, creationDate text)''')


def insert_card_into_cards_table(cursor, cardId, photoUrl, name, description, timestamp):
    cursor.execute(
        "INSERT INTO cards VALUES (?, ?, ?, ?, ?)", (cardId, photoUrl, name, description, timestamp))


def delete_card_from_cards_table(cursor, connection, cardId):
    cursor.execute("DELETE FROM cards WHERE cardId = ?", (cardId))
    save_data(connection)


def find_card_in_cards_table(cursor, cardId):
    card = cursor.execute(
        "SELECT * FROM cards WHERE cardId = ?", (cardId)).fetchone()
    return(card)


def close_connection(connection):
    connection.close()


def get_all_cards(cursor):
    cards = cursor.execute("SELECT * FROM cards").fetchall()
    return cards
