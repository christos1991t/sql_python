import sqlite3 as sq

connection = sq.connect("data.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM events WHERE band = 'Lion'")
result1 = cursor.fetchall()


print(result1)
