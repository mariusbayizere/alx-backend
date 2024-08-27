#!/usr/bin/env python3
"""
Flask app with Babel for internationalization
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Config class to set available languages and default locale and timezone
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
    The root route renders the index.html template.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
