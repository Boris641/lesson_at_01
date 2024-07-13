
import unittest
from Lesson_at_01 import add, subtract, multiply, divide

class TestMath(unittest.TestCase):
   def test_add(self):
       self.assertEqual(add(2, 5),7)
       self.assertNotEqual(add(3, 7), 9)

   def test_subtract(self):
       self.assertEqual(subtract(7, 4), 3)
       self.assertNotEqual(subtract(4, 2), 1)


   def test_multiply(self):
       self.assertNotEqual(multiply(2, 5), 1)
       self.assertEqual(multiply(3, 6), 18)

   def test_divide(self):
       result, remainder = divide(10, 3)
       self.assertAlmostEqual(result, 10 / 3)
       self.assertEqual(remainder, 10 % 3)

   def test_divide_zero_divisor(self):
       with self.assertRaises(ValueError):
           divide(10, 0)

   def test_divide_negative_numbers(self):
       result, remainder = divide(-10, 3)
       self.assertAlmostEqual(result, -10 / 3)
       self.assertEqual(remainder, -10 % 3)

       result, remainder = divide(10, -3)
       self.assertAlmostEqual(result, 10 / -3)
       self.assertEqual(remainder, 10 % -3)

       result, remainder = divide(-10, -3)
       self.assertAlmostEqual(result, -10 / -3)
       self.assertEqual(remainder, -10 % -3)

   def test_divide_zero_numerator(self):
       result, remainder = divide(0, 3)
       self.assertEqual(result, 0)
       self.assertEqual(remainder, 0)



if __name__ == '__main__':
   unittest.main()





