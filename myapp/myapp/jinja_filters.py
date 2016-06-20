# !usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2016-06-20 09:47:26
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2016-06-20 09:48:02

from __future__ import print_function, division, absolute_import
import numpy as np
import flask
import jinja2


# If the filter is to return HTML code and you don't want it autmatically
# escaped, return the value as "return Markup(value)".

jinjablue = flask.Blueprint('jinja_filters', __name__)

# Ref: http://stackoverflow.com/questions/12288454/how-to-import-custom-jinja2-filters-from-another-file-and-using-flask


@jinja2.contextfilter
@jinjablue.app_template_filter()
def split(context, value, delim=None):
    '''Split a string based on a delimiter'''
    if not delim:
        delim = ' '
    return value.split(delim) if value else None

