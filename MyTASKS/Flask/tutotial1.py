from flask import Flask, render_template, request, redirect, url_for, session, flash
app = Flask(__name__)
app.secret_key = "hello"
@app.route("/index")
def home():
    return render_template("index.html", content="Index Page")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        flash("Please Log In!")
        return render_template("second.html")

@app.route("/user")    
def user():
    if "user" in session:
        user = session["user"]
        flash("You have logged in Already!")
        return f"<h1>Welcome\n{user}</h1>"
    else:
        flash("Please Log In first!")
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    flash("You have logged out")
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)