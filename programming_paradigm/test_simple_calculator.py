import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Expected output is 5
        self.assertEqual(self.calc.add(-1, 1), 0)  # Expected output is 0
        self.assertEqual(self.calc.add(-1, -1), -2)  # Expected output is -2
        self.assertEqual(self.calc.add(0, 0), 0)  # Expected output is 0

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Expected output is 2
        self.assertEqual(self.calc.subtract(3, 5), -2)  # Expected output is -2
        self.assertEqual(self.calc.subtract(-1, -1), 0)  # Expected output is 0
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Expected output is 0

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)  # Expected output is 6
        self.assertEqual(self.calc.multiply(-1, 1), -1)  # Expected output is -1
        self.assertEqual(self.calc.multiply(-1, -1), 1)  # Expected output is 1
        self.assertEqual(self.calc.multiply(0, 10), 0)  # Expected output is 0

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)  # Expected output is 2
        self.assertEqual(self.calc.divide(-6, 3), -2)  # Expected output is -2
        self.assertEqual(self.calc.divide(-6, -3), 2)  # Expected output is 2
        self.assertEqual(self.calc.divide(0, 1), 0)  # Expected output is 0
        self.assertIsNone(self.calc.divide(6, 0))  # Expected output is None (division by zero)

if __name__ == "__main__":
    unittest.main()
