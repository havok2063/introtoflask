# Intro to Flask

Python Dependendies
-------------------

Make sure that [Flask](https://pypi.python.org/pypi/Flask/) is installed:

    % sudo pip install Flask

If you are using the [Anaconda Python distribution](http://www.continuum.io), Flask is already installed; you can make sure you are running the current version with:

    % sudo conda update flask

This tutorial has these Python dependencies:

 * [Flask-JSGlue](http://stewartjpark.com/Flask-JSGlue/)

Install it:

    % sudo pip install Flask-JSGlue

A Simple Example
----------------

This single file appliation demonstrates basic concepts of Flask.  To run, simply type:

    python app.py

I've added a few command-line arguments to make it a bit more flexible:

    -d --debug - runs the app in debug mode
    -p --port [number] - specify a different port to run the app on other than the default port 5000

Try::

    python app.py -d -p 8000

A More Complex Application
--------------------------

This example demonstrates a possible layout for a full-fledged application.  The application is now packaged into a
module called myapp.

Try::

    python run_myapp.py -d -p 9000

The main Flask app is now defined inside a method called create_app, located within the modules __init__.py file.
This allows you to run many instances of the same application, using the run_app command.
