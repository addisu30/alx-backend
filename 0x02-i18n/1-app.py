#!/usr/bin/env python3
<<<<<<< HEAD
""" Basic Babel setup
"""
from flask import Flask
from flask_babel import Babel
from flask import render_template


class Config:
    """create a Config class that has a LANGUAGES
       class attribute equal to ["en", "fr"].
=======

"""
1. Basic Flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class.
>>>>>>> 0bd157e293095f9cba0611d331d08eb6f2938b2e
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


<<<<<<< HEAD
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def hello() -> str:
    """The home/index page.
=======
app.config.from_object(Config)


@app.route('/', methods=["GET"], strict_slashes=False)
def hello():
    """
    hello.
>>>>>>> 0bd157e293095f9cba0611d331d08eb6f2938b2e
    """
    return render_template('1-index.html')


<<<<<<< HEAD
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
>>>>>>> 0bd157e293095f9cba0611d331d08eb6f2938b2e
