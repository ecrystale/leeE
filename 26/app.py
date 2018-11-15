'''
Emily Lee
SoftDev1 pd6
K#25 -- Getting More REST
2018-11-15
'''

import json
import urllib.request

from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def Hello_world():
    url_stub="http://api.nytimes.com/svc/topstories/v2/home.json?api-key="
    key="ed4eb13cfbb047da88ca5ab676989676"
    req=urllib.request.urlopen(url_stub+key)
    fin=json.loads(req.read())

    for i in fin["results"]:
        
    return render_template("index.html",
                               url=fin["results"]["url"],
                               title=fin["results"]["title"],
                               abstract=fin["results"]["abstract"])

if __name__=="__main__":
    app.debug=True
    app.run()
