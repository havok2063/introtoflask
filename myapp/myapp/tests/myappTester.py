# !usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2016-06-19 18:46:30
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2016-06-19 19:44:03

from __future__ import print_function, division, absolute_import

import json
import flask

try:
    from myapp import create_app
except ImportError as e:
    raise ImportError('Must set path to introtoflask/myapp in your PYTHONPATH')

try:
    from flask_testing import TestCase
except ImportError as e:
    TestCase = None


class MyAppTester(TestCase):
    ''' subclass (MarvinTester.MarvinTester, TestCase), in that order '''

    def create_app(self):
        app = create_app(debug=True)
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
        return app

    def setUp(self):
        self.longMessage = True
        self.response = None
        self.data = None
        self.insp_session = {}

    def tearDown(self):
        pass

    def _loadPage(self, type, page, params=None):
        if type == 'get':
            self.response = self.client.get(page)
        elif type == 'post':
            self.response = self.client.post(page, data=params)

