# Intro to Flask

Python Dependendies
-------------------

Make sure that [Flask](https://pypi.python.org/pypi/Flask/) is installed:

    % sudo pip install Flask

If you are using the [Anaconda Python distribution](http://www.continuum.io), Flask is already installed; you can make sure you are running the current version with:

    % sudo conda update flask

This tutorial has these Python dependencies:

 * [Flask-JSGlue](http://stewartjpark.com/Flask-JSGlue/) - this lets me use Flask url_for inside javascript
 * [Flask-Testing](https://pythonhosted.org/Flask-Testing/) - this makes it (a bit) easier to unit test your app

Install them:

    % sudo pip install Flask-JSGlue
    % sudo pip install Flask-Testing

Follow along with the code and the [IntroToFlask](introtoflask.pdf) slides.

Add the following to your PYTHONPATH in your .bashrc, .profile, or .tschrc

    export PYTHONPATH=$PYTHONPATH:/your/path/to/this/repo/introtoflask/myapp

and replace your/path/to/this/repo with your directory path.  Do this if you want your app to behave as a Python package, and to be able to import parts of it here and there.

A Simple Example
----------------

This single file appliation demonstrates basic concepts of Flask.  To run, simply type:

    python app.py

I've added a few command-line arguments to make it a bit more flexible:

    -d --debug - runs the app in debug mode
    -p --port [number] - specify a different port to run the app on other than the default port 5000

Try:

    python app.py -d -p 8000

In debug mode, the Flask app will auto-reload when it detects code changes, and provides full tracebacks in the
browser for easy debugging and development.  Let's work in debug mode from here on!

In the browser, now navigate to http://localhost:8000/

A More Complex Application
--------------------------

This example demonstrates a possible layout for a full-fledged application.  The application is now packaged into a
module called myapp.

Try:

    python run_myapp.py -d -p 9000

The main Flask app is now defined inside a method called create_app, located within the module's init file.
This allows you to run many instances of the same application, using the run_app command.

create_app is a way of creating an 'application factory'.  It allows you to test running your app under different configurations

In the browser, now navigate to http://localhost:9000/myapp/
