class Employee:
    
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
    
    @staticmethod    
    def from_string(s):
        fn,ln,sl = s.split('-')
        return Employee(fn,ln,sl)
