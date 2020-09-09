import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        drink_1 = Drink("Elven Wine", 9.99)
        drink_2 = Drink("Dwarf Ale", 10.99)
        self.drink = [drink_1, drink_2]
    
    # def test_drink_has_name(self):
    #     self.assertEqual("Elven Wine", self.drink.name)

    # def test_drink_has_price(self):
    #     self.assertEqual(9.99, self.drink.price)