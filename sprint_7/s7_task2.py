class Goods: 
  
    def __init__(self, price, discount_strategy = None):
        self.price = price
        self.discount_strategy = discount_strategy 
          
    def price_after_discount(self): 
        if not self.discount_strategy:
            discount = 0
        else:
            discount = self.discount_strategy(self)
        return self.price - discount
          
    def __str__(self):
        return f'Price: {self.price}, price after discount: {self.price_after_discount()}'
    
def on_sale_discount(order): #50%
    return order.price * 0.5
      
def twenty_percent_discount(order): #20%
    return order.price * 0.2
