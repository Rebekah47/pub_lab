class Customer:
    def __init__(self, input_name, input_wallet, input_age):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.drunkness_level = 0

    def reduce_wallet(self, drink):
        self.wallet -= drink.price

    def buy_drink(self, customer, pub, drink):
        customer.reduce_wallet(drink)
        pub.increase_till(drink)

    def customer_over_age(self, customer):
        if customer.age >= 18:
            return True
        else:
             return False
    
    def drunkness_level_increase(self, customer, drink):
        customer.drunkness_level += drink.alcohol_level
        