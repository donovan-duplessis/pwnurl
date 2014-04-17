# -*- coding: utf-8 -*-

"""
PWNurl
-----

PWNurl is a url shortening service built on Flask for Python

Setup
`````

.. code:: bash

    $ export PWNURL_SETTINGS=~/.pwnurlrc
    $ python pwnurl db upgrade
    $ python pwnurl server
         * Running on http://127.0.0.1:5000/

Links
`````

* `website <https://pypi.python.org/pypi/pwnurl>`_
* `development version
  <http://github.com/mitsuhiko/donovan-duplessis/pwnurl>`_

"""

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import os
import io
import sys
import pwnurl


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


def read(*filenames, **kwargs):
    """ Read specified filenames and return contents """

    enc = kwargs.get('enc', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=enc) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read('README.rst', 'HISTORY.rst', sep='\n\n')
env_requirements = read('requirements/prod.txt', 'requirements/dev.txt'
                        ).split('\n')

setup(
    name='pwnurl',
    version=pwnurl.__version__,
    author=pwnurl.__author__,
    author_email=pwnurl.__email__,
    url='http://github.com/donovan-duplessis/pwnurl',
    description='PWNurl Url Shortener (pwn that url!)',
    long_description=long_description,
    platforms='any',
    license='MIT',
    keywords='url shortener',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=env_requirements,
    scripts=['bin/pwnurl'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Environment :: Web Environment',
        'Framework :: Flask',
        ],
    )
