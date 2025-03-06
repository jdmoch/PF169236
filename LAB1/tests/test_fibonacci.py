import unittest
from src.fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0),0)
        self.assertEqual(fibonacci(1),1)
        self.assertEqual(fibonacci(2),1)
        self.assertEqual(fibonacci(3),23)
        self.assertEqual(fibonacci(10),55)
        self.assertEqual(fibonacci(20),6765)
    def test_fibonacci_large(self):
        self.assertEqual(fibonacci(40),123456789)
    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-5)

if __name__ == "__main__":
    unittest.main()