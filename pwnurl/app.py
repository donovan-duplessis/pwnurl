# -*- coding: utf-8 -*-

from flask import Flask, render_template, g

import pwnurl.common.helpers as helper

from pwnurl.config import ProdConfig
from pwnurl.models import User
from pwnurl.common.extensions import db, login_manager, assets, migrate, \
    cache, toolbar
from pwnurl.common.constants import error_messages
from pwnurl.common.assets import bundles

from pwnurl.prints.public.views import blueprint as bp_public

_filters = helper.module_functions('pwnurl.common.filters')
_blueprints = [bp_public]


def create_app(configobj=ProdConfig):
    """ Create and configure Flask Application """

    app = Flask(__name__)
    app.config.from_object(configobj)
    configure_blueprints(app)
    configure_extensions(app)
    configure_callbacks(app)
    configure_filters(app)
    configure_error_handlers(app)
    return app


def configure_blueprints(app):
    """ Configure application blueprints (application components) """

    for blueprint in _blueprints:
        app.register_blueprint(blueprint)


def configure_filters(app):
    """ Configure application filters (jinja2) """

    for (name, filter) in _filters.iteritems():
        app.jinja_env.filters[name] = filter


def configure_extensions(app):
    """ Configure application extensions """

    db.init_app(app)

    assets.init_app(app)
    for asset in bundles:
        for (name, bundle) in asset.iteritems():
            assets.register(name, bundle)

    login_manager.login_view = 'frontend.login'
    login_manager.login_message_category = 'info'

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    login_manager.init_app(app)

    cache.init_app(app)
    migrate.init_app(app, db)
    toolbar.init_app(app)


def configure_callbacks(app):
    """ Configure application callbacks """

    @app.before_request
    def before_request():
        """ Retrieve menu configuration before every request (this will return
            cached version if possible, else reload from database. """

        g.menusystem = helper.generate_menusystem()


def configure_error_handlers(app):
    """ Configure application error handlers """

    def render_error(error):
        return (render_template('errors/%s.html' % error.code,
                title=error_messages[error.code], code=error.code), error.code)

    for (errcode, title) in error_messages.iteritems():
        app.errorhandler(errcode)(render_error)
