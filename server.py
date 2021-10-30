from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    return f"Hello {name}"

@app.route("/contact")
def contact():
    return "<h1>Contact us</h1>"

app.run(debug=True, host="0.0.0.0")