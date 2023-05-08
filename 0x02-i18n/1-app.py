#!/usr/bin/env python3
"""Task 1 Module"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """Basic Flask app"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')