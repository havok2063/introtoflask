#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function, division, absolute_import
from flask import current_app, Blueprint, render_template, abort
from flask import session as current_session, request, redirect, url_for, jsonify

# this is a Blueprint.  It helps you modularize your app.
# This is the simplest way to use them. You can also specify a modular static and template folder
# index_page = Blueprint("index_page", __name__,
#               static_folder='relative/path/to/index/static/files',
#               template_folder='relative/path/to/index/template/files')
index_page = Blueprint("index_page", __name__)


# All defined routes should be attached to this Blueprint

@index_page.route('/', methods=['GET'])
def index():
    ''' This is the Main page.  I run every time someone (re)loads this page.

    Now that I'm a blueprint, you build my url as blueprint_name.method_name or
    blueprint_name.endpoint , e.g. index_page.index

    '''

    # Create a dictionary to contain all the parameters you want
    # to pass into the Jinja2 template
    output = {}
    output['title'] = 'MyApp'
    output['page'] = 'index'
    output['mytext'] = 'Here is some text!'
    if 'loadcat' not in current_session:
        current_session['loadcat'] = False
    print('loadcat is currently', current_session['loadcat'])
    output['myurl'] = url_for('index_page.index')

    # render_template accepts multiple keywords and arguments, but I like to keep everything together
    # in a single dictionary and the dump the contents into the template with **dict
    return render_template('index.html', **output)


@index_page.route('/idontexist/', endpoint='wrongpage')
def this_is_the_wrong_page():
    '''
    Use abort to raise an HTTP Exception for a given status code
    This redirects to your designated error_handler
    '''
    try:
        return render_template('wrongpage.html')
    except Exception as e:
        abort(404)


@index_page.errorhandler(404)
def page_not_found(e):
    ''' I'm a custom error handler for this blueprint only
    '''
    error = {}
    error['title'] = 'Index | Page Not Found'
    error['page'] = 'Custom Index Blueprint error: {0}'.format(request.url)
    return render_template('errors/page_not_found.html', **error), 404

