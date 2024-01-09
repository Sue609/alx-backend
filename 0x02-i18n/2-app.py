#!/usr/bin/env python3
'''
This mudule introduces a flask app
'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''
    Function that creates a get_ locale with the babel.
    localeselector decorator
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''
    Rendering the template
    '''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
