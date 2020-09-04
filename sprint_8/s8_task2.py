import unittest

class DivideTest(unittest.TestCase):

    tests = {   10.0 : [10, 1],
                2.5 : [5, 2],
                1.0 : [1, 1]
            }
    
    def test_positive_number_division(self):
        for answer,(num1, num2) in self.tests.items():
            with self.subTest(answer = answer):
                res = divide(num1, num2)
                self.assertEqual(res, answer)

        
    def test_div_by_zero(self):
        with self.assertRaises(Exception) as exc:
            res = divide(12,0)
            self.assertEqual("Division by zero", str(exc.exception))
            
    def test_negative_number_division(self):
        res = divide(-1000,8)
        self.assertEqual(res, -125.0)
