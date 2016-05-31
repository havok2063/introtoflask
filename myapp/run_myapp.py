#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function, division
import argparse
from myapp import create_app

# --------------------------
# Parse command line options
# --------------------------
parser = argparse.ArgumentParser(description='Script to start Flask app.')
parser.add_argument('-d', '--debug', help='Launch app in debug mode.', action="store_true", required=False)
parser.add_argument('-p', '--port', help='Port to use in debug mode.', default=5000, type=int, required=False)

args = parser.parse_args()

# ------------------
# My Flask App
# ------------------
app = create_app(debug=args.debug)

# ------------------
# Start the app
# ------------------
if __name__ == "__main__":
    app.run(debug=args.debug, port=args.port)


