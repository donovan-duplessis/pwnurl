#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import shlex
import subprocess

import pwnurl.common.helpers as h

from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import MigrateCommand
from flask.ext.assets import ManageAssets

from pwnurl import __version__ as ver
from pwnurl.app import create_app
from pwnurl.models import User, Role
from pwnurl.config import configs

from pwnurl.common.extensions import assets, db
from pwnurl.common.gunicorn_server import GunicornServer
from pwnurl.common.populate_manager import manager as populate_manager

phelp = """
Python
======
  locals: %s
"""

shelp = \
    """
SQLAlchemy
==========
  query:
    User.query.all()
    User.query.filter_by(id=1).first().username
"""

env = os.environ.get('PWNURL_ENV', 'dev')
app = create_app(configs[env])

if os.environ.get('PWNURL_SETTINGS', None):
    app.config.from_envvar('PWNURL_SETTINGS')

manager = Manager(app)

def config(key):
    """ Return app configuration value based on specified key """

    return app.config.get(key.upper(), None)


@manager.command
def test():
    """ Run all Tests [nose] """

    command = 'nosetests --with-coverage --cover-package=pwnurl'
    status = subprocess.call(shlex.split(command))
    sys.exit(status)


@manager.command
def profile(length=25):
    """ Start the application under the code profiler """

    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length])
    app.run()


def _help():
    """ Display both SQLAlchemy and Python help statements """

    statement = '%s%s' % (shelp, phelp % ', '.join(cntx_.keys()))
    print statement.strip()


cntx_ = dict(app=app, db=db, User=User, Role=Role, help=_help, h=h)
shell = dict(
    make_context=lambda: cntx_,
    banner='Interactive PwnUrl Shell v%s [type help() for help sheet]' % ver
)

bind_options = (config('host'), config('port'))

manager.add_command('gunicorn', GunicornServer(*bind_options))
manager.add_command('server', Server(*bind_options))
manager.add_command('assets', ManageAssets(assets))
manager.add_command('shell', Shell(**shell))
manager.add_command('db', MigrateCommand)
manager.add_command('populate', populate_manager)

if __name__ == '__main__':
    manager.run()
