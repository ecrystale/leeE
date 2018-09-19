'''
Emily Lee
SoftDevl pd6
K08 -- Fill Yer Flask
2018-9-18
'''

from flask import Flask
app=Flask(__name__)

@app.route("/") #creates default route
def hello_world():  #specific to the route before it only
    return "HW#8 first route"

@app.route("/elee") #adding "/elee" at the end changes the website
def hello_world2():
    return "HW#8 second route"

@app.route("/19") #"/19" = another website 
def hello_world3():
    return "HW#8 third route"

app.run() #gives only the default route
