import unittest
import pytest
from factory import NaanFactory


class TestFactory(unittest.TestCase):
    factory_test = NaanFactory()

    def test_make_dough(self):
        self.assertEqual(self.factory_test.make_dough('water', 'flour'), 'dough')

    def test_bake_dough(self):
        self.assertEqual(self.factory_test.bake_dough(True), 'naan')

