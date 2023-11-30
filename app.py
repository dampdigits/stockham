"""Temporary flask application"""

from flask import Flask, render_template , redirect , request ,url_for,session
from flask_mysqldb import MySQL

app = Flask(__name__)
# app.secret_key=""
# Session(app)


# session["user_id"] = "563"
# session["user_name"] = "sam"

app.config["MYSQL_HOST"]= "localhost"
app.config["MYSQL_USER"]= "root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]= "stockham"

mysql=MySQL(app)

@app.route("/")
def index():
    """Default route"""
    if "username" in session:
        return render_template("index.html",username=session["username"])
    else:
        return render_template("index.html")

@app.route("/register",methods=['GET','POST'])
def register():
    """Default route"""
    if request.method == "POST":
        username= request.form["username"]
        pwd=request.form["password"]

        cur=mysql.connection.cursor()
        cur.execute(f"insert into users(username,password) values ('{username}','{pwd}')")
        mysql.connection.commit()
        cur.close()

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    """Default route"""
    if request.method == "POST":
        username = request.form["username"]
        pwd = request.form["password"]
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT username, password FROM users WHERE username = '{username}'")
        user = cur.fetchone()
        cur.close()

        if user and pwd == user[1]:
            session["username"] = user[0]
            return redirect(url_for('index'))
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")

@app.route("/deposit")
def deposit():
    """Default route"""

    return render_template("deposit.html")

@app.route("/withdraw")
def withdraw():
    """Default route"""

    return render_template("withdraw.html")



if __name__=="__main__":
    app.run(debug=True)
