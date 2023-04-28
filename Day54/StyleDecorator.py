from flask import Flask
from markupsafe import escape

app = Flask(__name__)


def add_h1(function):
    def wrapper():
        old_text = function()
        return f"<h1> {old_text} </h1>"

    return wrapper


def add_underline(function):
    def wrapper():
        old_text = function()
        return f"<u> {old_text} </u>"

    return wrapper


def add_em(function):
    def wrapper():
        old_text = function()
        return f"<em> {old_text} </em>"

    return wrapper


@app.route("/")
@add_h1
@add_em
@add_underline
def hello_world():
    return "hello, world"


@app.route("/<path:name>/<int:age>")
def say_hello_to(name, age):
    return f"hello {escape(name)}, happy {escape(age)} Birthday."


if __name__ == "__main__":
    app.run()
