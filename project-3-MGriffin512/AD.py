# adding data
import sqlite3

connection = sqlite3.connect("army_ops.sql")
cursor = connection.cursor()

table = input("Which table: ")

if table == "division":
    name = input("Name: ")
    cursor.execute("Insert into divsion Values (?)"), (name,)
if table == "battalion": 
    name = input("Name: ")
    division_id = input("DIvision ID: ")
    cursor.execute("Insert into battalion (name, battalion_id) Values (?, ?)", (name, division_id))
if table == "soldier": 
    first = input("First name: ")
    last = input("Last name: ")
    rank = input("rank: ")
    battalion_id = input("Battalion ID: ")
    cursor.execute("Insert into soldier (first_name, last_name, rank, battalion_id) Values (?, ?, ?, ?)", (first, last, rank, battalion_id))
if table == "mission":
    name = input("Mission name: ")
    cursor.execute("Insert into mission (mission_name_ Values (?)", (name,))
if table == "assignmnet":
    soldier_id = input("Soldier ID: ")
    mission_id = input("Mission ID: ")
    status = input("Status: ")
    cursor.execute("Insert into assignment (soldier_id, mission_id, status) Values (?, ?, ?)", (soldier_id, mission_id, status))

connection.commit()
connection.close()