import unittest

from demo.test import calculate_gpa

if True:
    def hello():
        print("Hello World!")

class TestGPA(unittest.TestCase):
    def test_gpa_above_90(self):
        self.assertEqual(calculate_gpa(95), 4.0)

    def test_gpa_above_80(self):
        self.assertEqual(calculate_gpa(85), 3.0)

    def test_gpa_above_70(self):
        self.assertEqual(calculate_gpa(75), 2.0)

    def test_gpa_above_60(self):
        self.assertEqual(calculate_gpa(65), 1.0)

    def test_gpa_below_60(self):
        self.assertEqual(calculate_gpa(55), 0.0)

    def test_gpa_negative(self):
        with self.assertRaises(ValueError):
            calculate_gpa(-1)
    
    def test_gpa_invalid(self):
        self.assertIsNone(calculate_gpa("abc"))
    
    def test_gpa_invalid_2(self):
        self.assertIsNone(calculate_gpa(101))
