import unittest
from hw_14_task_1 import NegativeValueError, Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(5)
        self.r2 = Rectangle(3, 4)

    def test_width(self):
        self.assertEqual(self.r1.width, 5)

    def test_height(self):
        self.assertEqual(self.r2.height, 4)


    def test_perimeter(self):
        self.assertEqual(self.r1.perimeter(), 20)


    def test_area(self):
        self.assertEqual(self.r2.area(), 12)

    def test_addition(self):
        r3 = self.r1 + self.r2
        self.assertEqual(r3.width, 8)
        self.assertEqual(r3.height, 9.0)

if __name__ == '__main__':
    unittest.main()
