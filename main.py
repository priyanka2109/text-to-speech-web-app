from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator
app = Flask(__name__, static_folder='static')



@app.route("/")
def home():
    return render_template("index.html")
@app.route("/About")
def about():
    return render_template("About.html")

@app.route("/Contact")
def contact():
    return render_template("Contact.html")


if __name__ == "__main__":
    app.run()
