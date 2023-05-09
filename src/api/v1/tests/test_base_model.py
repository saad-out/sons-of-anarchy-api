"""
The `test_base_model` module defines unit tests for the `BaseModel` class in the `base_model` module.

The TestBaseModel class defines a set of unit tests for the `BaseModel` class. These tests are used to ensure that
the `BaseModel` class is working as expected.

Usage:
    To run the unit tests for this module, simply run the following from the project's src/ directory:
        
        $ python3 -m unittest api/v1/tests/test_base_model.py       # or python
    
    Note: this module requires the `unittest` package to be installed.
        
References:
    - unittest: https://docs.python.org/3/library/unittest.html
"""
import unittest
from datetime import datetime

from api.v1.models import BaseModel


class TestBaseModel(unittest.TestCase):
    """"
    Define a set of unit tests for the `BaseModel` class.
        
    This class defines a set of unit tests for the `BaseModel` class. These tests are used to ensure that the `BaseModel` class is working as expected.
        
    Setup:
        The `setUp` method is used to define instructions that will be executed before each test method.
        In this case, we are creating a new instance of the `BaseModel` class that can be used in each test method.
    """
    def setUp(self):
        self.base_model = BaseModel()

    def test_record_id(self):
        self.assertIsNotNone(self.base_model.recordId)
        self.assertIsInstance(self.base_model.recordId, str)
        self.assertEqual(len(self.base_model.recordId), 36)
    
    def test_created_at(self):
        self.assertIsNotNone(self.base_model.createdAt)
        self.assertIsInstance(self.base_model.createdAt, datetime)
        self.assertEqual(self.base_model.createdAt, self.base_model.updatedAt)

    def test_updated_at(self):
        self.assertIsNotNone(self.base_model.updatedAt)
        self.assertIsInstance(self.base_model.updatedAt, datetime)
        self.assertEqual(self.base_model.createdAt, self.base_model.updatedAt)


if __name__ == '__main__':
    unittest.main()
