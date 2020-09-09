import unittest

from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Elven Wine", 9.99, 12)        
        self.customer = Customer("Aragorn", 100.00, 72)
        self.pub = Pub("The Prancing Pony", 100, self.drink)

    def test_customer_name(self):
        self.assertEqual("Aragorn", self.customer.name)

    def test_customer_wallet(self):
        self.assertEqual(100.00, self.customer.wallet)
    
    def test_reduce_wallet(self):
        self.customer.reduce_wallet(self.drink)
        self.assertEqual(90.01, self.customer.wallet)
    
    def test_buy_drink(self):
        self.customer.buy_drink(self.customer, self.pub, self.drink)
        self.assertEqual(90.01, self.customer.wallet)
        self.assertEqual(109.99, self.pub.till)

    def test_customer_has_age(self):
        self.assertEqual(72, self.customer.age)

    def test_customer_over_age(self):
        self.customer = Customer("Frodo", 20, 12)
        self.assertEqual(False, self.customer.customer_over_age(self.customer))
    
    def test_customer_drunk_level(self):
        self.assertEqual(0, self.customer.drunkness_level)   

    def test_customer_drunk_level_inrease(self):
        self.customer.drunkness_level_increase(self.customer, self.drink)
        self.assertEqual(12, self.customer.drunkness_level)
