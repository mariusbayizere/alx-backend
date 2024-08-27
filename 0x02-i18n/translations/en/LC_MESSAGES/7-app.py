#!/usr/bin/env python3
"""
Flask app with Babel for internationalization, locale, and timezone selection.
"""

from flask import Flask, render_template, request
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError

app = Flask(__name__)

class Config:
    """
    Config class to set available languages, default locale, and timezone.
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
    If a locale is passed as a URL parameter, use that instead.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    """
    Determines the best match for supported timezones based on the request.
    If a timezone is passed as a URL parameter, use that instead.
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone)
        except UnknownTimeZoneError:
            pass  # If timezone is invalid, fall through to the next option
    # Implement user timezone retrieval logic here, if applicable.
    return app.config['BABEL_DEFAULT_TIMEZONE']

@app.route('/')
def index():
    """
    The root route renders the index.html template.
    """
    return render_template('7-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
