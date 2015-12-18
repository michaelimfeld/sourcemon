# -*- coding: utf-8 -*-
"""
    Main application
"""

from flask import Flask
from sourcemon.routes import api

STATIC_PATH = "/static"

app = Flask(__name__, static_url_path=STATIC_PATH)
app.register_blueprint(api)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
