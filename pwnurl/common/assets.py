# -*- coding: utf-8 -*-

from flask.ext.assets import Bundle

bundles = [
    dict(css_all=Bundle(
        "libs/bootstrap/dist/css/bootstrap.css",
        "css/style.css",
        filters="cssmin",
        output="public/css/common.css")
    ),
    dict(js_all=Bundle(
        "libs/jQuery/dist/jquery.js",
        "libs/bootstrap/dist/js/bootstrap.js",
        "js/plugins.js",
        filters='jsmin',
        output="public/js/common.js")
    )
]
