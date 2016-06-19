# !usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2016-06-19 18:48:53
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2016-06-19 20:00:40

from __future__ import print_function, division, absolute_import

import os
import flask
import json
import unittest
import myappTester
from flask import url_for
from flask import session


class TestIndexPage(myappTester.MyAppTester):

    def test_index_status_code_ok(self):
        ''' test a status 200 OK '''
        with self.app.app_context():
            self._loadPage('get', url_for('index_page.index'))
            self.assertStatus(self.response, 200, 'MyApp"s index page should return a good status of 200')

    def test_index_status_code_bad(self):
        ''' test a 404 page not found '''
        with self.app.app_context():
            self._loadPage('get', 'iamthewrongpage')
            self.assertStatus(self.response, 404, 'MyApp"s index page should return a bad status of 404')

    # should be in its own test_example.py page but I'm getting lazy
    def test_example_changesession(self):
        ''' tests that a method in examples.py can successfully change the session '''

        # set the initial loadcat in the session
        self._loadPage('get', url_for('index_page.index'))
        # change the loadcat session variable - toggling on
        params = {'isactive': 'false'}
        self._loadPage('post', url_for('example_page.changesession'), params=params)

        # this nested with blocks tells the testing suite to hold on to the app context
        # app.test_context() is stored as self.client
        with self.client as c:
            # this with tells the testing suite to open the app session and allow for modifications to it
            with c.session_transaction() as sesh:
                # asserting the return session variable is True
                self.assertTrue(sesh['loadcat'])


if __name__ == '__main__':
    # set to 1 for the usual '...F..' style output, or 2 for more verbose output.
    verbosity = 2
    unittest.main(verbosity=verbosity)


