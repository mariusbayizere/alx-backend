#!/usr/bin/env python3
"""Application that enforces locale selection via URL parameters."""

from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel


class AppConfig:
    """Configuration class for the Flask application."""

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(AppConfig)
app.url_map.strict_slashes = False
babel = Babel(app)

user_data = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def retrieve_user() -> Union[Dict, None]:
    """Fetches the user information based on the user ID provided
    """
    user_id = request.args.get('login_as')
    if user_id:
        return user_data.get(int(user_id))
    return None


@app.before_request
def before_request_handler() -> None:
    """Executed before each request to set the user context."""
    g.current_user = retrieve_user()


@babel.localeselector
def select_locale() -> str:
    """Determines the locale to be used for rendering
    """
    url_locale = request.args.get('locale')
    if url_locale in app.config['LANGUAGES']:
        return url_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def homepage() -> str:
    """Renders the homepage.
    """
    return render_template("5-index.html)


if __name__ == "__main__":
    app.run()
