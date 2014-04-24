# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located
in app.py
"""

from flask.ext.login import LoginManager
login_manager = LoginManager()

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.migrate import Migrate
migrate = Migrate()

from flask.ext.cache import Cache
cache = Cache()

from flask.ext.assets import Environment
assets = Environment()

from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension()
