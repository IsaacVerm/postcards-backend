import sqlite3

conn = sqlite3.connect('postcards.db')

c = conn.cursor()

# c.execute('''CREATE TABLE cards
#              (year text, description text, country text)''')

# c.execute("INSERT INTO cards VALUES ('1991', 'A nice card', 'Belgium')")

# conn.commit()
# conn.close()

print(c.execute("SELECT * FROM cards").fetchall())
