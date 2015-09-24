#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from manstein import config
from manstein.utils import config_from_env


def configure_app(app, **kwargs):
    # default configuration
    app.config.from_object(config)
    app.config.update(config_from_env('MANSTEIN_'))
    app.config.update(kwargs)


def configure_extensions(app):
    try:
        from flask.ext.debugtoolbar import DebugToolbarExtension
        # debug toolbar; it's automatically disabled if DEBUG == False
        DebugToolbarExtension(app)
    except ImportError:
        pass


def create_app(**kwargs):
    app = Flask(__name__)
    configure_app(app, **kwargs)
    configure_extensions(app)
    return app


if __name__ == '__main__':
    _app = create_app()
    _app.run(debug=True, host='0.0.0.0', port=5000)
