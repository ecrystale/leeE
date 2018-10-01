
from flask import Flask #, render_template
#from util import

app=Flask(__name__)
from flask import Flask, session, render_template, url_for, redirect, request
import os

app=Flask(__name__)
app.secret_key=os.urandom(32)

@app.route("/")
def login():
    return render_template("/practice.html")

@app.route("/welcome", methods=["POST"])
def auth():
    session["watermelon"]="juice"
    if request.form["user"]!="watermelon":
        return redirect(url_for("login"))
    if request.form["pass"]!=session["watermelon"]:
        return redirect(url_for("login"))
    if request.form["pass"]==session["watermelon"]:
        return render_template("/welcome.html")
        
if __name__=="__main__":
    app.debug=True
    app.run()
