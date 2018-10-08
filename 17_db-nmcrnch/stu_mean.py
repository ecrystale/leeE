#
#
#
#

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

def compAvg():
    grades = {}
    c.execute("SELECT * FROM peeps, courses WHERE peeps.id == courses.id;")
    rows = c.fetchall()
    for row in rows:
        if row[2] not in grades:
            counter = 1
            grades[row[2]] = [str(row[0]),row[4]]
        else:
            counter += 1
            grades[row[2]][1] = (grades[row[2]][1]*(counter-1) + row[4]) / counter
    return(grades)

def peeps_avg(grades):
    c.execute("CREATE TABLE peeps_avg(name STRING, avg INTEGER)")
    for idnum,avg in grades.items():
        c.execute("INSERT INTO peeps_avg VALUES(" + str(idnum) + ","+str(avg[1])+")")
#def display():

def addcourses(c,g,i):
    with open("data/courses.csv","a",newline='') as file:
        fields=["code","grade","idnum"]
        writer=csv.DictWriter(file,fieldnames=fields)
        writer.writerow({"code":str(c),"grade":str(g),"idnum":str(i)})
        
grades=compAvg()
print(grades)
peeps_avg(grades)
#addcourses("x",31,11)
db.commit() #save changes
db.close()  #close database
