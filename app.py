"""Temporary flask application"""

from flask import Flask, render_template
from flask_session.__init__ import Session

app = Flask(__name__)
Session(app)

# session["user_id"] = "563"
# session["user_name"] = "sam"


@app.route("/")
def index():
    """Default route"""

    return render_template("index.html")

@app.route("/register")
def register():
    """Default route"""

    return render_template("register.html")

@app.route("/login")
def login():
    """Default route"""

    return render_template("login.html")

@app.route("/deposit")
def deposit():
    """Default route"""

    return render_template("deposit.html")

@app.route("/withdraw")
def withdraw():
    """Default route"""

    return render_template("withdraw.html")
