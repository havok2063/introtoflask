#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function, division, absolute_import
from flask import Flask, url_for, redirect
import argparse

# --------------------------
# Parse command line options
# --------------------------
parser = argparse.ArgumentParser(description='Script to start Flask app.')
parser.add_argument('-d', '--debug', help='Launch app in debug mode.', action="store_true", required=False)
parser.add_argument('-p', '--port', help='Port to use in debug mode.', default=5000, type=int, required=False)

args = parser.parse_args()

# -------
# Flask App
# -------
app = Flask(__name__)


@app.route('/')
def main():
    ''' Main method routed to page "/"

        Navigating to '/' runs this method
        and returns results to the page
    '''
    return 'Hello, Welcome to Flask'


@app.route('/add/', endpoint='doadd')
@app.route('/addnumbers/')
def add():
    x = 1
    y = 2
    z = x + y
    return 'Adding: x+y: {0} + {1} = {2}'.format(x, y, z)


@app.route('/hello/<name>/')
@app.route('/hello/', defaults={'name': 'Bob'})
def hello(name):
    ishello = g.get('hello', None)
    return 'Hello {0}, also {1}'.format(name, ishello)


@app.route('/subtract/<int:x>/<int:y>/', methods=['GET'], endpoint='dosubtract')
def subtract(x, y):
    ''' Subtract method with variables

    You can convert variables into different types on input with
        <converter:variable>

    Built-In Converter types:
        int - convert to integer
        float - convert to float
        string - accepts text without trailing slash
        path - accepts text with slashes

    '''
    z = x - y
    return 'Subtracting x-y: {0} - {1} = {2}'.format(x, y, z)


@app.route('/addagain/', endpoint='letsaddagain')
def do_more_adding():
    '''
    We can redirect from a route to another using
    named endpoints, url_for, and redirect

    Navigate to /addagain/ and it redirects to the /add/ page
    '''

    addurl = url_for('doadd')
    print('Add URL:', addurl, url_for('add'))
    print('Subtract URL:', url_for('dosubtract', x=10, y=3))
    return redirect(addurl)


@app.route('/crash/', endpoint='crash')
def crash_me():
    '''
    In debug mode, when a crash occurs, a full traceback is sent
    to the webpage

    Also debug mode comes with a reloader, so changes in the code are auto
    updated without having to stop and restart the app.

    '''

    # Try to expand a tuple that does not have all the things
    thing = (5, 4)
    x, y, z = thing

    return 'I have not crashed'


if __name__ == '__main__':
    app.run(port=args.port, debug=args.debug)



