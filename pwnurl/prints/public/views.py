# -*- coding: utf-8 -*-

""" Public Blueprint Views """

from flask import Blueprint, render_template

from pwnurl import basedir
from pwnurl.common.decorators import requires_roles, admin_required
import os

baseman = os.path.join(basedir, 'pwnurl', 'templates')

blueprint = Blueprint('public', __name__, static_folder='../static',
                      template_folder=baseman)


@blueprint.route('/', methods=['GET'])
@requires_roles('admin')
@admin_required
def home():
    return render_template('public/home.html')
