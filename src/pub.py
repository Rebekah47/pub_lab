from src.customer import *
from src.drink import *


class Pub:

    def __init__(self, input_name, input_till, input_drinks):
        self.name = input_name
        self.till = input_till
        self.drinks = input_drinks
    
    def increase_till(self, drink):
        self.till += drink.price
    
    def customer_over_age(self, customer):
        if customer.age >= 18:
            return True
        else:
             return False 