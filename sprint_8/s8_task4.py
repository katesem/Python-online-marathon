import unittest

class TriangleNotValidArgumentException(Exception):
    pass

class TriangleNotExistException(Exception):
    pass

class Triangle:
    def __init__(self, *args):
        try:
            if  len(args) != 3 or not all(isinstance(item, int) for item in args): #not valid args
                raise TriangleNotValidArgumentException
            a,b,c = args
            if a < 0 or b < 0 or c < 0 or a + b < c or a + c < b or b + c < a:
                raise TriangleNotExistException
            self.a, self.b, self.c = args
            self.area = self.get_area()
        except (TriangleNotValidArgumentException, TriangleNotExistException ):
            print('Can`t create triangle with this arguments')
                
    def get_area(self):
        p = (self.a + self.b + self.c)/ 2
        s = (p * (p-self.a) * (p-self.b) * (p-self.c))** 0.5
        return (float(str(s)[: str(s).index('.')+3]) if str(s)[0] != 0 else s)


class TriangleTest(unittest.TestCase):
    
    valid_test_data = [
    ((3, 4, 5), 6.0),
    ((10, 10, 10), 43.30),
    ((6, 7, 8), 20.33),
    ((7, 7, 7), 21.21),
    ((50, 50, 75), 1240.19),
    ((37, 43, 22), 406.99),
    ((26, 25, 3), 36.0),
    ((30, 29, 5), 72.0),
    ((87, 55, 34), 396.0),
    ((120, 109, 13), 396.0),
    ((123, 122, 5), 300.0)
]
    not_valid_triangle = [
    (1, 2, 3),
    (1, 1, 2),
    (7, 7, 15),
    (100, 7, 90),
    (17, 18, 35),
    (127, 17, 33),
    (145, 166, 700),
    (1000, 2000, 1),
    (717, 17, 7),
    (0, 7, 7),
    (-7, 7, 7)
]  
    not_valid_arguments = [
        ('3', 4, 5),
        ('a', 2, 3),
        (7, "str", 7),
        ('1', '1', '1'),
        'string',
        (7, 2),
        (7, 7, 7, 7),
        'str',
        10,
        ('a', 'str', 7)
    ]

    def test_valid_args(self):
        for i in range(len(self.valid_test_data)):
            with self.subTest(): 
                valid_obj = Triangle(self.valid_test_data[i][0][0], self.valid_test_data[i][0][1], self.valid_test_data[i][0][2])
                self.assertEqual(valid_obj.area, self.valid_test_data[i][1]) #OK

    def test_not_valid_args(self):
        for i in range(len(self.not_valid_arguments)):
            with self.subTest(): 
                not_valid_args = Triangle(self.not_valid_arguments[i])
                
        
    def test_not_valid_triangle(self):
        for i in range(len(self.not_valid_triangle)):
            with self.subTest(): 
                not_valid_tr = Triangle(self.not_valid_triangle[i])
                
unittest.main()
