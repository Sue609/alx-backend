#!/usr/bin/env python3
"""
Module that introduces a flask app
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """
    Babel configurations
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    function with the babel.localeselector decorator
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index() -> str:
    """
    The home router
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)