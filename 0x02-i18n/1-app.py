#!/usr/bin/env python3
'''
This module introduces a flask app
'''
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    '''
    Flask babel configurations
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def greeting():
    '''
    Function that says hello world
    '''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
