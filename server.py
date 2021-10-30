from flask import Flask, request, render_template,url_for, redirect
import database as db
app = Flask(__name__)

@app.route("/sample")
def index():
    name = request.args.get("name")
    return f"Hello {name}"

@app.route("/")
def landing():
    return render_template("index.html")


@app.route("/addPassword", methods=['GET',"POST"])
def addPassword():
    if request.method == "GET":
        status = request.args.get("status")
        passwords = db.getPasswords()
        return render_template("addPassword.html", status=status, passwords=passwords)
    else:
        url = request.form['url']
        password = request.form['password']
        status = db.addPassword(url, password)
        return redirect(url_for("addPassword",status=status))


@app.route("/contact")
def contact():
    return "<h1>Contact us</h1>"

app.run(debug=True, host="0.0.0.0")