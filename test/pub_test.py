import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
import pdb

class TestPub(unittest.TestCase):
    def setUp(self):
        # self.drink = [{"name": "Elven Wine", "price": 9.99}, {"name": "Dwarf Ale", "price": 10.99}]
        drink_1 = Drink("Elven Wine", 9.99, 12)
        drink_2 = Drink("Dwarf Ale", 10.99, 6)
        self.drink = [drink_1, drink_2]
        self.pub = Pub("The Prancing Pony", 100, self.drink)

    def test_pub_has_name(self):
        pub_name = self.pub.name
        self.assertEqual("The Prancing Pony", pub_name)
    
    def test_pub_has_till(self):
        pub_till = self.pub.till
        self.assertEqual(100, pub_till)

    def test_increase_till(self):
        self.pub.increase_till(self.drink[0])
        self.assertEqual(109.99, self.pub.till)
    
    def test_pub_has_drink(self):
        self.assertEqual(2, len(self.drink))
    
    def test_drink_name(self):
        self.assertEqual("Elven Wine", self.drink[0].name)
    
    