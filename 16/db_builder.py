#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

c.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

command = "("
with open("peeps.csv", newline='') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        command = "INSERT INTO students VALUES"
        # print (row["name"], row["age"], row["id"])
        command += "(" + row['id'] + ", \"" + row['name'] + "\", " + row['age'] + ");"
        c.execute(command)
        # print(command)

#==========================================================

db.commit() #save changes
db.close()  #close database


