from flask import Flask,render_template, request, redirect, url_for,session

app = Flask(__name__)

app.secret_key = "hello"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method =="POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        # if "user" in session:
        #     return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))
@app.route("/logout")
def log_it():
    session.pop["us11   r", None]
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug=True)

    