#!/usr/bin/python3
"""Unittest for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def setUP(self):
        pass

    def tearDown(self):
        pass

    def test_docstring(self):
        self.assertIsNotNone(max_integer.__doc__)

    def test_lists(self):
        self.assertEqual(max_integer([0, 1, 40, 3]), 40)
        self.assertEqual(max_integer([-5, 3, 5]), 5)
        self.assertEqual(max_integer([69,96, 6, 9]), 96)
        self.assertEqual(max_integer([69, 99, 9]), 99)
        self.assertEqual(max_integer([4]), 4)

    def test_strings(self):
        self.assertEqual(max_integer(["a", "z"]), "z")

    def test_negative_float(self):
        self.assertEqual(max_integer([-5.55, -66.66, -111.1]), -5.55)

    def test_not_same_datatypes(self):
        with self.assertRaises(TypeError):
            max_integer([1, "1"])

    def test_empty(self):
        self.assertEqual(max_integer([]), None)
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list_list(self):
        self.assertEqual(max_integer([[1, 2], [2, 1]]), [2, 1])


if __name__ == "__main__":
    unittest.main()
