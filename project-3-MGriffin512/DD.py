#Display an overview
import sqlite3

connection = sqlite3.connect("army_ops.sql")
cursor = connection.cursor()

cursor.execute("SELECT soldier.first_name, soldier.last_name, soldier.rank, battalion.name, division.name FROM soldier JOIN battalion ON soldier.battalion_id = battalion.battalion.battalion_id JOIN divsion ON battalion.division_id = division.divsion_id")
               
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()