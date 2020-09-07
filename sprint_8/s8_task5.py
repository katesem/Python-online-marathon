import unittest
class Worker:
    
    def __init__(self, name = None, salary = 0):
        if salary < 0 :
            raise  ValueError
        self.name = name
        self.salary = salary
        
    def get_tax_value(self): #calculate tax from salary 
        tax = 0
        cur_salary = self.salary
        summa_list = [1000, 3000, 5000, 10000, 20000, 50000, 1000000]
        percentage = [0, 0.1, 0.15, 0.21, 0.3, 0.4, 0.47]
        for summa, percent in zip(summa_list, percentage):
            if cur_salary > 0: 
                if cur_salary >= summa:
                    tax += summa * percent
                    cur_salary -= summa
                else:
                    tax += cur_salary * percent
                    break
        return tax
            

class WorkerTest(unittest.TestCase):
    
    def setUp(self):    # preparing to test
        self.worker = Worker('Kate', 1001)
        
    @unittest.expectedFailure
    def test_taxes_amount(self):
         self.assertEqual(0.1, self.worker.get_tax_value())
         
    def tearDown(self):  # ending the test
        self.worker = None
