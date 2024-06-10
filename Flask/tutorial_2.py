#variables in Flask

from flask import Flask
app= Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return "HELLO %s" %name

@app.route('/blog/<postID>') 
def show_blog(postID): 
    return 'Blog Number %d' %int(postID) 

@app.route('/rev/<revNo>') 
def revision(revNo): 
    return 'Revision Number %f' %float(revNo) 

if __name__=="__main__":
    app.run(debug = True) 