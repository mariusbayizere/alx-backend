#!/usr/bin/env python3
"""
Flask app with Babel for internationalization and locale selection.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

class Config:
    """
    Config class to set available languages and default locale and timezone.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale():
    """
    Determines the best match for supported languages based on the request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """
    The root route renders the 3-index.html template.
    """
    return render_template('3-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
