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
    url_stub="http://www.asterank.com/api/skymorph/search?target="
    target="J99TS7A"
    
    req=urllib.request.urlopen(url_stub+target)
    fin=json.loads(req.read())

    key=fin["results"][0]["key"]
    
    url_stub="http://www.asterank.com/api/skymorph/image?key="
    return render_template("index.html",
                                   url=url_stub+key)

if __name__=="__main__":
    app.debug=True
    app.run()
