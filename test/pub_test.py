import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Elven Wine", 9.99)
        self.pub = Pub("The Prancing Pony", 100, self.drink)

    def test_pub_has_name(self):
        pub_name = self.pub.name
        self.assertEqual("The Prancing Pony", pub_name)
    
    def test_pub_has_till(self):
        pub_till = self.pub.till
        self.assertEqual(100, pub_till)

    def test_increase_till(self):
        self.pub.increase_till(self.drink)
        self.assertEqual(109.99, self.pub.till)

