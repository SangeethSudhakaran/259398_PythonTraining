import sqlite3

connection = sqlite3.connect("Chinook_Sqlite.sqlite")
curr = connection.cursor()

print(curr)

curr.execute("select name from sqlite_master where type = 'table';")
tables = curr.fetchone()

for table in tables:
    print(table)

curr.execute("select * from album limit 10")
tables = curr.fetchall()

desc = curr.description
cols = [col[0] for call in desc]

print(cols)

for table in tables:
    print(table)