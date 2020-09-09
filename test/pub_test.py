import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        drink_1 = Drink("Elven Wine", 9.99)
        drink_2 = Drink("Dwarf Ale", 10.99)
        self.drink = [drink_1, drink_2]
        self.pub = Pub("The Prancing Pony", 100.00, self.drink)

    def test_pub_has_name(self):
        pub_name = self.pub.name
        self.assertEqual("The Prancing Pony", pub_name)
    
    def test_pub_has_till(self):
        pub_till = self.pub.till
        self.assertEqual(100.00, pub_till)
    
    # def test_pub_drinks(self):
    #     self.assertEqual(2, len(self.drink))

    # def test_increase_till(self):
    #     self.assertEqual(109.99, increase_till(self, drink))

