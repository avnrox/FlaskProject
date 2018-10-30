from flask import Flask, redirect, url_for,render_template
app=Flask(__name__)
@app.route("/")
def index():
    name = "Python flask Workshop"
    return render_template("tmp2.htm2",name1=name)
@app.route("/list")
def list():
           a=[111,222,333,444]
           return render_template("tmp2.html",name2=a)
@app.route("/dict")
def dict():
           dict={"0":"arjun","1":"blah","2":"bleh"}
           return render_template("tmp2.html",name3=dict)
if __name__ == "__main__":
    app.run(debug=True)
