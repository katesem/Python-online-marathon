import unittest
import math

def quadratic_equation(a, b, c):
    d = (float(b)** 2) - 4 * float(a) * float(c)
    if d < 0 :
        return
    if a == 0:
        raise ValueError
    
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    if x1 == x2:
        return x1
    return x1, x2

class QuadraticEquationTest(unittest.TestCase):
    def test_discriminant_equals_zero(self):
        test1 = quadratic_equation(1, 6, 9)
        self.assertEqual(test1, -3)
        
    def test_discriminant_greater_than_zero(self):
        test2 = quadratic_equation(2, 1, -1)
        self.assertEqual(test2, (0.5, -1.0))
        
    def test_discriminant_less_than_zero(self):
        test3 = quadratic_equation(2, 4, 7)
        self.assertEqual(test3, None)
        
    def test_big_numbers(self):
        test4 = quadratic_equation(100, 200, -300)
        self.assertEqual(test4, (1.0, -3.0))
