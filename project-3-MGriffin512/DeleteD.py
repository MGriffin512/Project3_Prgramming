# Delete Data
import sqlite3

connection = sqlite3.connect("army_ops.sql")
cursor = connection.cursor()

table = input("Table: ")
id_column = table + "_id"
row_id = input("Row ID: ")

okay = input ("If you want deleted, type YES: ")
if okay == "YES":
    cursor.execute(f"Delete from {table}, Where {id_column} = ?", (row_id,))
    connection.commit()

connection.close()