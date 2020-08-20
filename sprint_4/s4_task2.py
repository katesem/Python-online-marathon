class Pizza:
    order_number = 0 # class variable
    
    def __init__(self,ingredients = []):
        self.ingredients = ingredients
        Pizza.order_number += 1
        self.order_number = Pizza.order_number
    
    @staticmethod
    def hawaiian():
        return Pizza(['ham','pineapple'])
        
    @staticmethod
    def garden_feast():
        return Pizza(['spinach', 'olives', 'mushrooms'])
    
    @staticmethod
    def meat_festival():
        return Pizza(['beef','meatball', 'bacon'])
