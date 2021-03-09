from flask import Flask, render_template, request
from data import data


app = Flask(__name__)
app.config.from_pyfile("config.py")


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/user/<int:user_id>")
def user(user_id):
    # pass a dict to the template
    # keep order in toy data now but getting would prob be handled by say mongodb
    user_data = data[user_id - 1]  # bc int is positive
    return render_template("user.html", user_data=user_data)


if __name__ == "__main__":
    app.run()