import sqlite3

class Database:

    def __init__(self, db):
        global conn
        conn = sqlite3.connect(db)
        global cur
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        conn.commit()

    def insert(self, title, author, year, isbn):
        cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        conn.commit()

    def view(self):
        cur.execute("SELECT * FROM book")
        rows=cur.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows = cur.fetchall()
        return rows

    def delete(self, id):
        cur.execute("DELETE FROM book WHERE id=?", (id,))
        conn.commit()

    def update(self, id, title, author, year, isbn):
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", ( title, author, year, isbn, id))
        conn.commit()



# insert("The Sun", "John Smith", 1918, 9191282817)
# delete(2)
# update(4, "The moon", "George Pig", 2020, 99999999999)
# print(view())
# print(search(author="John Smith"))