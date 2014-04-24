# -*- coding: utf-8 -*-

""" Helper utilities and decorators """

import inspect

from flask import flash
from importlib import import_module
from collections import OrderedDict

from pwnurl.common.extensions import cache


def module_functions(modulestr):
    """ Return ordered dictionary of all functions declared in module """

    funcs = dict(inspect.getmembers(import_module(modulestr),
                 inspect.isfunction))

    return OrderedDict(sorted(funcs.items(), key=lambda f: f[0]))


def flash_errors(form, category='warning'):
    """ Flash all form error messages """

    for (field, errors) in form.errors.items():
        for error in errors:
            flash('{0} - {1}'.format(getattr(form, field).label.text, error),
                  category)


@cache.cached(timeout=31557600, key_prefix='menusystem')
def generate_menusystem():
    """ """

    pass
