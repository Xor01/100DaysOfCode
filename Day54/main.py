# guessing-the-number game using Flask
import random

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

flag = random.randint(0, 9)


@app.route("/")
def guess_the_number():
    return "<h1>guess a number between 0 and 9 !</h1>" \
           '<iframe src="https://giphy.com/embed/3ov9k1lJ0A2o4OQew8" width="400" height="400" frameBorder="0" ' \
           'class="giphy-embed" allowFullScreen></iframe>'


@app.route("/<int:guess>")
def check_guess(guess):
    if guess == flag:
        return "<h1 style='color:green'>Yee!! your answer is correct</h1>" \
               "<img src='https://media2.giphy.com/media/1DTBGm5Rfgymk/giphy.gif?cid" \
               "=ecf05e477v3axel6h9fiqp3qh4apq96twsentzb91idquk4h&ep=v1_gifs_search&rid=giphy.gif&ct=g'/>"
    return '<h1 style="color: purple">Too high, try again!</h1> <img ' \
           'src="https://media0.giphy.com/media/S4506EKbdGFGSkOHBV/giphy.gif?cid' \
           '=ecf05e479weu0ursf6c1pdyrfh6t47f358je2leoafs3g7vx&ep=v1_gifs_search&rid=giphy.gif&ct=g" />' \
        if guess > flag else \
        '<h1 style="color: red">Too Low, try again!</h1>' \
        '<img src="https://media0.giphy.com/media/11IYKJ5sN73twk/giphy.gif?cid' \
        '=ecf05e47g6nu4v6au30ywqv3vojfauiqw8zdqqvoz2awk00c&ep=v1_gifs_search&rid=giphy.gif&ct=g">'


if __name__ == "__main__":
    app.run(debug=True)
