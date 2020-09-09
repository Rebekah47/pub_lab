import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Elven Wine", 9.99, 12)
        
    
    def test_drink_has_name(self):
        self.assertEqual("Elven Wine", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(9.99, self.drink.price)
        
    def test_drink_has_alcohol(self):
        self.assertEqual(12, self.drink.alcohol_level)