from flask import Flask
app= Flask(__name__)


@app.route("/")
def hello():
    return "HELLO"


@app.route("/hello")
def helloworld():
    return "HELLO WORLD"

@app.route("/joe")
def hello_joe():
    return "HELLO Joe"
app.add_url_rule("/", "joe", hello_joe)




if __name__=="__main__":
    app.run(debug = True) 
