from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/user/<int:user_id>")
def user(user_id):
    return render_template("user.html", user_id=user_id)


if __name__ == "__main__":
    app.run()