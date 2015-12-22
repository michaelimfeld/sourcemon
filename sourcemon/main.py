#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Main application
"""

from flask import Flask
from sourcemon.routes import api

app = Flask(__name__, static_folder="/var/www/sourcemon/static")
app.register_blueprint(api)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
