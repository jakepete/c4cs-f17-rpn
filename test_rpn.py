import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3, rpn.calculate('2 1 +'))

    def test_sub(self):
        self.assertEqual(1, rpn.calculate('2 1 -'))
