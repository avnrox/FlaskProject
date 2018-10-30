from flask import Flask
app=Flask(__name__)

@app.route ("/")
def hello():
        return "Hello World"
@app.route("/about/<name>")

def about(name):
        return "BLAH BLEH BLAH %s!" %name
@app.route("/about/<int:age>")
def hi(age):
        return "hi your age is %d!" %age

if __name__ == "__main__":
        app.run(debug = True)
        
