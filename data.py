import sqlite3

db_ = sqlite3.connect('database.db')

db = db_.cursor()
# db.execute("DROP TABLE app")
# db.execute("""CREATE TABLE app (title TEXT NOT NULL, description TEXT NOT NULL, url TEXT, id INTEGER  PRIMARY KEY AUTOINCREMENT)""")
db.execute("ALTER TABLE app ADD mark INTEGER NOT NULL DEFAULT 0")


db_.commit()
