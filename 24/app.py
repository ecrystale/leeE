'''
Emily Lee
SoftDev1 pd6
K<n> -- <Title/Topic/Summary>
2018-<mm>-<dd>
'''

from flask import Flask, session, render_template, url_for, redirect, request, flash
import os
#from util import

app=Flask(__name__)
app.secret_key=os.urandom(32)

app=Flask(__name__)

@app.route("/")
def Hello_world():
    return "Welcome"

if __name__=="__main__":
    app.debug=True
    app.run()
