# -*- coding: utf-8 -*-
import unittest
#from nose.tools import *  # PEP8 asserts

from pwnurl.database import db
from pwnurl.user.models import User
from .base import DbTestCase
from .factories import UserFactory


class TestUser(DbTestCase):

    def test_factory(self):
        user = UserFactory(password="myprecious")
        self.assertTrue(user.username)
        self.assertTrue(user.email)
        self.assertTrue(user.created_at)
        self.assertFalse(user.is_admin)
        self.assertTrue(user.active)
        self.assertTrue(user.check_password("myprecious"))

    def test_check_password(self):
        user = User.create(username="foo", email="foo@bar.com",
                    password="foobarbaz123")
        self.assertTrue(user.check_password('foobarbaz123'))
        self.assertFalse(user.check_password("barfoobaz"))

    def test_full_name(self):
        user = UserFactory(first_name="Foo", last_name="Bar")
        self.assertEqual(user.full_name, "Foo Bar")

if __name__ == '__main__':
    unittest.main()
