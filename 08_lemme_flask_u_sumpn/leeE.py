'''
Emily Lee
SoftDevl pd6
K08 -- Fill Yer Flask
2018-9-18
'''

from flask import Flask
app=Flask(__name__)

#route links
def first():
    return '<a href="/"> First Route </a>'

def second():
    return '<a href="/elee"> Second Route </a>'

def third():
    return '<a href="/19"> Third Route </a>'

@app.route("/")
def hello_world(): #words on pages + links
    return "HW#8 first route <br/><br/>"+second()+"<br/><br/>"+third()

@app.route("/elee") #different route
def hello_world2():
    return "HW#8 second route <br/><br/>"+first()+"<br/><br/>"+third()

@app.route("/19") 
def hello_world3():
    return "HW#8 third route <br/><br/>"+first()+"<br/><br/>"+second()

app.run()
