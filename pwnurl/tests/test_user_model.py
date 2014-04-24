from pwnurl.models import User

from pwnurl.tests.base import DbTestCase


class UserModelTestCase(DbTestCase):

    def test_password_setter(self):
        u = User(password='cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='cat')
        with self.assertRaises(AttributeError):
            u.password
