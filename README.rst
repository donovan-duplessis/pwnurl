******************************
PWNurl: url shortening service
******************************

.. image:: https://badge.fury.io/py/pwnurl.png
    :target: http://badge.fury.io/py/pwnurl

.. image:: https://travis-ci.org/donovan-duplessis/pwnurl.png?branch=master
        :target: https://travis-ci.org/donovan-duplessis/pwnurl

**Table of Contents**


.. contents::
    :local:
    :depth: 1
    :backlinks: none

=============
Main Features
=============

* TODO

============
Installation
============

The **latest stable version** can always be installed or updated to via `pip`_:

.. code-block:: bash

    $ pip install --upgrade pwnurl


The **latest development version** can be installed directly from GitHub:
|travis-master|

.. |travis-master| image:: https://travis-ci.org/donovan-duplessis/pwnurl.png?branch=master
    :target: https://travis-ci.org/donovan-duplessis/pwnurl
    :alt: Build Status of the master branch


.. code-block:: bash

    $ pip install --upgrade https://github.com/donovan-duplessis/pwnurl/tarball/master

=============
Configuration
=============

You need to set the ``PWNURL_SETTINGS`` environment variable to point to the
configuration file:

.. code-block:: bash

    $ export PWNURL_SETTINGS=~/.pwnurlrc

The following configuration parameters are vailable:

+-------------------------+-----------------------------------------------------------------+
| Parameter               | Description                                                     |
+=========================+=================================================================+
| HOST                    | Hostname or ip address to bind server on                        |
|  ``name=string``        |   e.g. ``HOST = '0.0.0.0'``                                     |
+-------------------------+-----------------------------------------------------------------+
| PORT                    | Port number to bin server on                                    |
|  ``name=integer``       |   e.g. ``PORT = 5001``                                          |
+-------------------------+-----------------------------------------------------------------+
| SECRET_KEY              | Secret application key/token                                    |
|  ``name=sring``         |   e.g. ``SECRET_KEY = 'yU2Tz4PVMVWlDNceFuH'``                   |
+-------------------------+-----------------------------------------------------------------+
| CACHE_TYPE              | Caching implementation (simple|memcached|redis)                 |
|  ``name=string``,       |   e.g. ``CACHE_TYPE = 'simple'``                                |
+-------------------------+-----------------------------------------------------------------+
| SQLALCHEMY_DATABASE_URI | Database connection string                                      |
|  ``name=string``        |   e.g. ``SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/pwnurl.db'`` |
+-------------------------+-----------------------------------------------------------------+

=====
Usage
=====


Initialize Database:

.. code-block:: bash

    $ pwnurl db upgrade

Compile Web Assets:

.. code-block:: bash

    $ pwnurl assets clean
    $ pwnurl assets build

Start Gunicorn Server:

.. code-block:: bash

    $ pwnurl gunicorn [--daemon]

Stop Gunicorn Server:

.. code-block:: bash

    $ kill -TERM `cat /tmp/pwnurl.pid`

=======
Authors
=======

`Donovan du Plessis`_  (`@binarytrooper`_)

=======
Licence
=======

Please see `LICENSE`_.

------

.. _pip: http://www.pip-installer.org/en/latest/index.html
.. _Donovan du Plessis: http://binarytrooper.com
.. _@binarytrooper: https://twitter.com/binarytrooper
.. _AUTHORS.rst: https://github.com/donovan-duplessis/pwnurl/blob/master/AUTHORS.rst
.. _LICENSE: https://github.com/donovan-duplessis/pwnurl/blob/master/LICENSE
