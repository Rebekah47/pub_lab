class Customer:
    def __init__(self, input_name, input_wallet, input_age):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.drunkness_level = 0

    def reduce_wallet(self, drink):
        self.wallet -= drink.price

    def customer_over_age(self, customer):
        if customer.age >= 18:
            return True
        else:
             return False
        