#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function, division
from flask import current_app, Blueprint, render_template, session as current_session, request, redirect, url_for, jsonify

index_page = Blueprint("index_page", __name__)


@index_page.route('/', methods=['GET'])
def index():
    ''' This is the Main page '''

    # Create the dictionary to contain all the values
    output = {}
    output['title'] = 'MyApp'
    output['page'] = 'index'
    output['mytext'] = 'Here is some text!'

    return render_template('index.html', **output)



