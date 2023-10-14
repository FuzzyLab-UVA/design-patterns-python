from faker import Faker

fake = Faker()

class CalculateShippingSpy(object):

    def __init__(self):
        self.entry = dict()

    def execute_calculation(self, order, shipping):
        self.entry['order'] = order
        self.entry['shipping'] = shipping
        total = shipping.calculate(order)
        return total