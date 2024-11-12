import convert
import unittest

class TestCases(unittest.TestCase):

    def test_str_to_float_1(self):
        input = "Hello"
        output = convert.str_to_float(input)
        expected = None
        self.assertEqual(expected, output)
    def test_str_to_float_2(self):
        string = "1.23"
        output = convert.str_to_float(string)
        expected = 1.23
        self.assertEqual(expected, output)