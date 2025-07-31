from flask import Flask, url_for, render_template
from markupsafe import escape


name = 'James'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html", name=name, movies=movies)

@app.route("/test01/<name>")
def test01_page(name):
    # return f"user1: {escape(name)}"
    return f"user1: {name}"

@app.route("/test02")
def test02_page():
    print("url for home_page:", url_for("home_page"))
    return "test02"