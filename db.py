import sqlite3


def create_postcards_connection():
    connection = sqlite3.connect('postcards.db')
    return connection


def create_cursor(connection):
    cursor = connection.cursor()
    return cursor


def create_cards_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS cards
             (year text, description text, country text)''')


def insert_values_into_cards_table(cursor, year, description, country):
    cursor.execute(
        "INSERT INTO cards VALUES ('1991', 'A nice card', 'Belgium')")


def save_data(connection):
    connection.commit()


def close_connection(connection):
    connection.close()


def get_all_cards(cursor):
    cards = cursor.execute("SELECT * FROM cards").fetchall()
    return cards
