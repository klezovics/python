import unittest
from add import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,1),2)
        self.assertEqual(add(2,3),5)

    