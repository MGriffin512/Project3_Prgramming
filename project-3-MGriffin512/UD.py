# Update 
import sqlite3

connection = sqlite3.connect("army_ops.sql")
cursor = connection.cursor()

table = input("Table: ")
id_column = table + "_id"
row_id = input("Row ID: ")
column = input("Column: ")
value = input("New value: ")

cursor.execute(f"Update {table} set {column} = ? Where {id_column} = ?", (value, row_id))
connection.commit()
connection.close()