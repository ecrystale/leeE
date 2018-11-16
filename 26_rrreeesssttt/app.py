'''
Emily Lee
SoftDev1 pd6
K#26 -- Getting More REST
2018-11-16
'''

import json
import urllib.request

from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def Hello_world():
    #Top Story
    url_stub="http://api.nytimes.com/svc/topstories/v2/home.json?api-key="
    key="ed4eb13cfbb047da88ca5ab676989676"
    req=urllib.request.urlopen(url_stub+key)
    fin=json.loads(req.read())

    #sunrise-sunset
    url_2="https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=today"
    req2=urllib.request.urlopen(url_2)
    fin2=json.loads(req2.read())

    #Cat_API
    cat_key="372def17-b796-46bd-a548-bf74a94e09df"
    url_3="https://api.thecatapi.com/v1/images/search?size=full&mime_types=jpg,png,gif&format=json&order=RANDOM&page=0&limit=10&category_ids&x-api-key="
    req3=urllib.request.urlopen(url_3+cat_key)
    fin3=json.loads(req3.read())
    
    return render_template("index.html",
                               url=fin["results"][0]["url"],
                               title=fin["results"][0]["title"],
                               abstract=fin["results"][0]["abstract"],
                               sunrise=fin2["results"]["sunrise"],
                               sunset=fin2["results"]["sunset"],
                               cat=fin3[0]["url"]
                            )



if __name__=="__main__":
    app.debug=True
    app.run()
