# !usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2016-06-19 18:36:54
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2016-06-19 18:39:21

from __future__ import print_function, division, absolute_import

from flask import Flask
from werkzeug.contrib.profiler import ProfilerMiddleware
from myapp import create_app
import argparse

# --------------------------
# Parse command line options
# --------------------------
parser = argparse.ArgumentParser(description='Script to start the SDSS API.')
parser.add_argument('-p', '--port', help='Port to use in debug mode.', default=5000, type=int, required=False)
args = parser.parse_args()


# Start the Profiler app and runs in DEBUG mode

app = create_app(debug=True)

app.config['PROFILE'] = True
app.wsgi_app = ProfilerMiddleware(app.wsgi_app)
app.run(debug=True, port=args.port)




