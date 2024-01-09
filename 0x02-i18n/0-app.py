#!/usr/bin/env python3
'''
This module introduces a flask app
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def greeting():
    '''
    Function that says hello world
    '''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
