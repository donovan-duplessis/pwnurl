# -*- coding: utf-8 -*-

import os


class Config(object):

    """ Base Configuration """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 't*wrw^(47u&n=a4)4$v4*vk2gfy-'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ECHO = False
    PORT = 5000
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LEVEL = 13
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):

    """ Production Configuration """

    DB_NAME = 'prod.db'
    DEBUG = False
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    DEBUG_TB_ENABLED = False


class DevConfig(Config):

    """ Development Configuration """

    DEBUG = True
    DB_NAME = 'dev.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    DEBUG_TB_ENABLED = True
    SQLALCHEMY_ECHO = True
    ASSETS_DEBUG = True
    CACHE_TYPE = 'simple'


class TestConfig(Config):

    """ Testing Configuration """

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


configs = {'dev': DevConfig, 'test': TestConfig, 'prod': ProdConfig}
