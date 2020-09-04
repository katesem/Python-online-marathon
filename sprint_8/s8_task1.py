import unittest

class Products:

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        self.price = self.calc_price()
    
    def calc_price(self):
        count_list = [2, 5, 7, 10, 20, 21] 
        discount_list = [0, 0.05, 0.1, 0.2, 0.3]
        for i in range(len(count_list) - 1):
            if self.count < count_list[i+1]:
                return self.price - self.price * discount_list[i]
            if self.count > 20:
                return self.price - self.price * 0.5
                
class Cart: 
    
    def __init__(self, *args):
        self.product = Products(*args)

class CartTest(unittest.TestCase):
    
    def setUp(self):
        self.cart = Cart('Apple', 10, 4)
        
    def test_equal_price(self):
        expected = 10
        self.assertEqual(expected, self.cart.product.price)
        
