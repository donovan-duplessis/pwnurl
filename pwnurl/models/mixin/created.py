# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql.expression import func

from pwnurl.common.extensions import db


class CreatedMixin(object):

    @declared_attr
    def created(cls):
        return db.Column(db.DateTime(timezone=True), default=func.now())
