'''
Emily Lee
SoftDev1 pd6
K#13 -- Echo Echo Echo
2018-09-27
'''

from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def Hello_world():
    return render_template("template.html")\
        +"<br><br><br><center>"\
        +"Method="+request.method\
        +"</center>"

@app.route("/auth", methods=['GET', 'POST'])
def hello():
    #inputs username from input
    if request.method == 'POST':
        return "<center><font size='5'>Welcome "\
            +(request.form["username"])\
            +"</font><br><br><br>"+\
            "Method="+request.method \
            +"<br><br><br>"\
            +"<a href='/'>New Username</a>"
    #if there's an error, back to homepage
    else:
        return "<center><a href='/'>Retry</a></center>"

if __name__=="__main__":
    app.debug=True
    app.run()
