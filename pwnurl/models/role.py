# -*- coding: utf-8 -*-

from pwnurl.common.extensions import db
from pwnurl.models.base import BaseModel


class Role(db.Model, BaseModel):

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    title = db.Column(db.String)
    default = db.Column(db.Boolean, default=False, index=True)

    users = db.relationship('User', backref='role', lazy='dynamic')
