from flask import Flask, redirect, url_for,render_template
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("tmp.html")
@app.route("/admin")
def hello_admin():
    return "Adminstrator Area, guest are not allowed"
@app.route("/guest/<guest>")
def hello_guest(guest):
    return "Guest User %s is not having admin rights"%guest
@app.route("/user/<user>")
def hello_user(name):
    if name=="admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest",guest=name))
if __name__ == "__main__":
    app.run(
        debug=True)
    
