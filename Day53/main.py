# Webdev Flask
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/<name>")
def hello_world(name):
    return f"Hello, World {escape(name)}"


def index():
    return 'Index Page'


app.route('/')(index)
# dec(index)
if __name__ == '__main__':
    app.run()
