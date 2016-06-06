#!/usr/bin/env python
# encoding: utf-8

from flask import request


def processRequest(request=None, raw=None):
    '''Generally process the request for POST or GET, and build a form dict

        Parameters:
            request (request):
                HTTP request object containing POST or GET data
            raw (bool):
                Boolean indicating whether to return the raw request data or not
        Returns:
            Dict or ImmutableMultiDict
    '''

    # get form data
    if request.method == 'POST':
        data = request.form
    elif request.method == 'GET':
        data = request.args
    else:
        return None

    # Return Raw Request Data
    if raw:
        return data

    # build form dictionary
    try:
        form = {key: val if len(val) > 1 else val[0] for key, val in data.iterlists()}
    except AttributeError:
        form = {key: val if len(val) > 1 else val[0] for key, val in data.lists()}

    return form
