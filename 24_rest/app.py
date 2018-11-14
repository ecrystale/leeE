'''
Emily Lee
SoftDev1 pd6
K#24 -- A RESTful Journey Skyward
2018-11-14
'''

from flask import Flask,render_template,redirect
import os, json
import urllib.request, urllib.parse
#from util import

app=Flask(__name__)
app.secret_key=os.urandom(32)

app=Flask(__name__)

@app.route("/")
def Hello_world():
    req=urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=MlnQPzS5RuJ7aNPok1wy6Z53cijvBjf8LjBaxBZW")
    fin=json.loads(req.read())
    for a in fin:
        if a=="url":
            return render_template("index.html",
                                   url=fin[a])

if __name__=="__main__":
    app.debug=True
    app.run()
