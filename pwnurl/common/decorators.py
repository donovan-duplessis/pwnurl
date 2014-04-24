# -*- coding: utf-8 -*-

from functools import wraps

from flask import abort
from flask.ext.login import current_user


def requires_roles(*roles):
    """ """

    def wrapper(f):

        @wraps(f)
        def wrapped(*args, **kwargs):
            try:
                if current_user.role.name not in roles:
                    abort(403)
            except AttributeError:
                pass
            return f(*args, **kwargs)
        return wrapped

    return wrapper


def admin_required(f):
    """ """

    return requires_roles('admin')(f)
