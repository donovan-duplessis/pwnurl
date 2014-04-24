#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Base model to inherit standard methods + crud functionality
"""

from pwnurl.common.extensions import db


class BaseModel(object):

    def __init__(self, **kwargs):
        """ Support variable length keyword arguments in constructor """

        for (key, value) in kwargs.iteritems():
            setattr(self, key, value)

    def __repr__(self):
        """ Display object string representation in format:
                <Model(table=models)>'
        """

        return "<%s(table='%s', id=%s)>" % (
            self.__class__.__name__, self.__table__, str(self.id))

    @classmethod
    def saveform(cls, form):
        """ Create and save form model data to database """

        columns = dict()
        for name, field in cls.form_fields.iteritems():
            columns[name] = getattr(form, field).data
        instance = cls(**columns)
        return instance.save()

    @classmethod
    def get_by_id(cls, id):
        """ Get model by identifier """

        if any((isinstance(id, basestring) and id.isdigit(), isinstance(id,
               (int, float)))):
            return cls.query.get(int(id))
        return None

    @classmethod
    def create(cls, **kwargs):
        """ Create and save model to database """

        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """ Update model attributes and save to database """

        for (attr, value) in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """ Save model to database """

        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """ Delete model from database """

        db.session.delete(self)
        return commit and db.session.commit()
