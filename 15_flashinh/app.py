#Cathy Cai and Emily Lee - CaiLee Cosmetics
#SoftDev1 pd6
#K15 -- Oh yes, perhaps I do...
#2018-10-03

from flask import Flask, session, render_template, url_for, redirect, request, flash
import os

app=Flask(__name__)
app.secret_key=os.urandom(32)


@app.route("/")
def login():
    #if logged in, welcome!
    if 'watermelon' in session:
        return render_template("/welcome.html",
                               user="Watermelon")

    #if not, log in!
    return render_template("/login.html")



@app.route("/welcome", methods=["POST"])
def auth():

    session["watermelon"]="juice" #hard code user and pass
            
        #wrong username/pass
    if request.form["user"]!="watermelon":
        flash('Wrong username or password!')
        session.pop("watermelon")
        return redirect(url_for("login"))
            
    if request.form["pass"]!=session["watermelon"]:
        flash('Wrong password!')
        session.pop("watermelon")
        return redirect(url_for("login"))

        
    #right username and pass, go to welcome page!
    if request.form["pass"]==session["watermelon"]:
        return render_template("/welcome.html",
                               user="Watermelon"
                               )




@app.route("/logout")
#logging out removes the user from the current session
def logout():
    session.pop("watermelon")
    return redirect(url_for("login"))


if __name__=="__main__":
    app.debug=True
    app.run()
