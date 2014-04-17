#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import shlex
import subprocess

from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import MigrateCommand
from flask.ext.assets import ManageAssets

from pwnurl import __version__ as ver
from pwnurl.app import create_app
from pwnurl.user.models import User
from pwnurl.assets import assets
from pwnurl.settings import DevConfig, ProdConfig
from pwnurl.database import db
from pwnurl.gunicorn_server import GunicornServer

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
cfg = (DevConfig if env == 'dev' else ProdConfig)
app = create_app(cfg)

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


def _help():
    """ Display both SQLAlchemy and Python help statements """

    statement = '%s%s' % (shelp, phelp % ', '.join(cntx_.keys()))
    print statement.strip()


cntx_ = dict(app=app, db=db, User=User, help=_help)
shell = dict(make_context=lambda: cntx_,
             banner='Interactive PwnUrl Shell v%s [type help() for help sheet]'
             % ver)

bind_options = (config('host'), config('port'))

manager.add_command('gunicorn', GunicornServer(*bind_options))
manager.add_command('server', Server(*bind_options))
manager.add_command('assets', ManageAssets(assets))
manager.add_command('shell', Shell(**shell))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
