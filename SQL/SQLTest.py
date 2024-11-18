import sqlite3

connection = sqlite3.connect("Chinook_Sqlite.sqlite")
curr = connection.cursor()

print(curr)

curr.execute("SELECT name FROM sqlite_master where type='table';")
tables = curr.fetchone()

for table in tables:
    print(table)

curr.execute("select * from album limit 10")
data = curr.fetchall()

desc = curr.description
cols = [col[0] for col in desc]

print(cols)

for table in tables:
    print(table)

for row in data:
    print(data)

