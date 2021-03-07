from flask import Flask, render_template
from data import data

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/user/<int:user_id>")
def user(user_id):
    # pass a dict to the template
    # keep order in toy data now but getting would prob be handled by say mongodb
    user_data = data[user_id - 1]  # bc int is positive
    return render_template("user.html", user_data=user_data)


if __name__ == "__main__":
    app.run()