import unittest
import pytest
from factory import NaanFactory


# Creating our testing class that inherits from the unittest Testcase framework
class TestFactory(unittest.TestCase):
    factory_test = NaanFactory()  # Creating an instance of the NaanFactory class to test its methods

    def test_make_dough(self):
        # Check if dough is output when water and flour are passed
        self.assertEqual(self.factory_test.make_dough('water', 'flour'), 'dough')
        self.assertEqual(self.factory_test.make_dough('flour', 'water'), 'dough')
        # Check if dough is output when anything other than water and flour are passed
        self.assertEqual(self.factory_test.make_dough('honey', 'meat'), 'this attempt to make dough has failed')

    def test_bake_dough(self):
        # Check if naan is created when bake_dough is called with successful dough (True)
        self.assertEqual(self.factory_test.bake_dough(True), 'naan')
        # Check if naan is created when bake_dough is called with unsuccessful dough (False)
        self.assertEqual(self.factory_test.bake_dough(False), 'this attempt to make naan has failed')
