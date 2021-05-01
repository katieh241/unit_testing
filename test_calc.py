import unittest
import calc

class TestCase (unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(3,5),8)

    def test_sub(self):
        self.assertEqual(calc.subtract(5,3),2)

    def test_divide(self):
        self.assertEqual(calc.divide(15,5),3)

    def test_multiply(self):
        self.assertEqual(calc.multiply(3,5),15)

    

if __name__ == '__main__':
    unittest.main(verbosity=2)