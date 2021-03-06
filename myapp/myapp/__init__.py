#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function, division, absolute_import
from flask import Flask, Blueprint, send_from_directory, request, render_template
from flask_jsglue import JSGlue
from myapp.jinja_filters import jinjablue

import sys
import os


def create_app(debug=False):

    # -----------------------------
    # Create App
    # -----------------------------
    # instantiate the Flask app, __name__ tells Flask what belongs to the application
    app = Flask(__name__, static_url_path='/static')
    app.debug = debug

    # I make it so you can build URLs in javascript using Flask's url_for
    # rather than having to hardcode anything.
    # http://stewartjpark.com/Flask-JSGlue/
    jsglue = JSGlue(app)

    # -----------------------------------
    # Set up a Logger for your application
    # -----------------------------------
    # log = standard Pythong logging thing you create here -- then add it to the Flask handler
    # app.logger.addHandler(log)
    # use your logger with app.logger.info('this is info'), don't use print statements inside Flask

    # ----------------------------------
    # Load an appropriate Flask configuration file for a debug or production version
    # ----------------------------------
    if app.debug:
        server_config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'configuration', 'localhost.cfg')
    else:
        pass
        # Load a configuration file for a production version of your app!
        # server_config_file = /path/to/production/config/file

    # app.logger.info('Loading config file: {0}'.format(server_config_file))
    app.config.from_pyfile(server_config_file)

    # ----------------------------
    # Manually add any configuration parameters
    # ----------------------------
    app.config["UPLOAD_FOLDER"] = os.environ.get("MYAPP_DATA_DIR", None)

    # ----------------------------
    # Global Error Handlers
    # ----------------------------
    @app.errorhandler(404)
    def this_is_the_wrong_page(e):
        error = {}
        error['title'] = 'MyApp | Page Not Found'
        error['page'] = request.url
        return render_template('errors/page_not_found.html', **error), 404

    # ----------------------------------
    # Web Route Registration - Import and register all your blueprints here
    # ----------------------------------
    from myapp.controllers.index import index_page
    from myapp.controllers.examples import example_page

    url_prefix = '/myapp'  # I can prefix all routes with a name
    app.register_blueprint(index_page, url_prefix=url_prefix)
    app.register_blueprint(example_page, url_prefix=url_prefix)

    # Register all custom Jinja filters in the file.
    app.register_blueprint(jinjablue)

    return app

