import unittest

from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Elven Wine", 9.99)        
        self.customer = Customer("Aragorn", 100.00)

    def test_customer_name(self):
        self.assertEqual("Aragorn", self.customer.name)

    def test_customer_wallet(self):
        self.assertEqual(100.00, self.customer.wallet)
    
    def test_reduce_wallet(self):
        self.customer.reduce_wallet(self.drink)
        self.assertEqual(90.01, self.customer.wallet)

    