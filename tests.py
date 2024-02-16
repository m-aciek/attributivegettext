from collections import UserString
from io import BytesIO
from unittest import TestCase

from translations import AttributiveTranslations

empty_mo_file = BytesIO(b'\x95\x04\x12\xde'  # magic number, same as gettext.GNUTranslations.LE_MAGIC.to_bytes(4, 'big')
                        b'\x00\x00\x00\x01'  # version
                        b'\x00\x00\x00\x00'  # msgcount
                        b'\x00\x00\x00\x00'  # masteridx
                        b'\x00\x00\x00\x00')  # transidx


class AttributiveTranslationsTest(TestCase):
    def setUp(self):
        empty_mo_file.seek(0)

    def test_value_returned_is_userstring(self):
        value_returned = AttributiveTranslations(empty_mo_file).gettext('foo')
        self.assertIsInstance(value_returned, UserString)

    def test_is_attributive(self):
        t = AttributiveTranslations(empty_mo_file)
        t._catalog = {'attribute\x04foo': 'bar'}

        foo = t.gettext('foo')
        self.assertEqual('bar', foo.attribute)

    def test_fallbacks(self):
        t = AttributiveTranslations(empty_mo_file)
        t._catalog = {'user': 'użytkownik'}

        message = t.gettext('user')
        result = message.samplecontext
        self.assertEqual('użytkownik', result)
