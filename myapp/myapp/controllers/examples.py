#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function, division
from flask import current_app, Blueprint, render_template, abort
from flask import session as current_session, request, redirect, url_for, jsonify
import numpy as np

# this is a Blueprint.  It helps you modularize your app.
example_page = Blueprint("example_page", __name__)


@example_page.route('/examples/')
def example():
    output = {}
    output['title'] = 'MyApp Examples'
    output['page'] = 'example'

    return render_template('examples.html', **output)


@example_page.route('/getrandomnumber/', methods=['POST'], endpoint='getrandom')
def getrandom():
    ''' Generates a Random Number

    This is function designed primarily with a handling an
    asynchronous javascript request from your browser.  It must
    return a JSON object

    Parameters:
        start (int): the starting value
        end (int): the ending value

    Returns:
        result (dict):

    '''
    result = {}
    result['number'] = np.random.random()
    result['error'] = None
    result['status'] = -1

    return jsonify(result=result)
