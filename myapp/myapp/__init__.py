#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function, division
from flask import Flask, Blueprint, send_from_directory
#import myapp.jinja_filters
import sys
import os


def create_app(debug=False):

    # -----------------------------
    # Create App
    # -----------------------------
    app = Flask(__name__, static_url_path='/static')
    app.debug = debug

    # Define custom filters into the Jinja2 environment.
    # Any filters defined in the jinja_env submodule are made available.
    # See: http://stackoverflow.com/questions/12288454/how-to-import-custom-jinja2-filters-from-another-file-and-using-flask
    #custom_filters = {name: function for name, function in getmembers(jinja_filters) if isfunction(function)}
    #app.jinja_env.filters.update(custom_filters)

    # -----------------------------------
    # Set up a Logger for your application
    # -----------------------------------
    # app.logger.addHandler(log)

    # ----------------------------------
    # Load the appropriate Flask configuration file for a debug or production version
    # ----------------------------------
    if app.debug:
        #server_config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'configuration', 'localhost.cfg')
        pass
    else:
        pass
        # Load a configuration file for a production version of your app!
        # server_config_file = /path/to/production/config/file

    #app.logger.info('Loading config file: {0}'.format(server_config_file))
    #app.config.from_pyfile(server_config_file)

    # ----------------------------
    # Manually add any configuration parameters
    # ----------------------------
    app.config["UPLOAD_FOLDER"] = os.environ.get("MYAPP_DATA_DIR", None)

    # ----------------------------------
    # Web Route Registration
    # ----------------------------------
    from myapp.controllers.index import index_page

    url_prefix = '/myapp/'
    app.register_blueprint(index_page, url_prefix=url_prefix)

    return app

