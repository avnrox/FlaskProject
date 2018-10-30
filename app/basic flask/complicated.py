from flask import Flask, redirect, url_for, render_template
app=Flask(__name__)
@app.route("/")
def index():
    user = {"username":"Dhiraj"}
    posts = [
        {
            "author":{"username":"Daniel"},
            "body":"Beutiful day in Sri lanka!"
        },
        {
            "author":{"username":"Amar"},
            "body":"Tiger Zinda hai movie was cool"
        }
        ]
    return render_template ("index.html",user=user,posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
