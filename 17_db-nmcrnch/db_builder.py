#StewMeen - Emily Lee, Ricky Lin
#SoftDev1 pd06
#K17: Average
#2018-10-09 T

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

open(DB_FILE,'w').close() #Reset DB file

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)"          #build SQL stmt, save as string
c.execute(command)    #run SQL statement

with open('data/peeps.csv','r') as csvfile:
    reader = csv.DictReader(csvfile) #Create csv dictionary
    for row in reader:
        #Add values into peeps table
        c.execute("INSERT INTO peeps VALUES(" + "'" + row['name'] + "'," + row['age'] + "," + row['id'] + ")")

c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)") #Make new table
with open('data/courses.csv','r') as csvfile:
    reader = csv.DictReader(csvfile) #Create csv dictionary
    for row in reader:
        #Add values into courses table
        c.execute("INSERT INTO courses VALUES(" + "'" + row['code'] + "'," + row['mark'] + "," + row['id'] + ")")

#==========================================================

db.commit() #save changes
db.close()  #close database
