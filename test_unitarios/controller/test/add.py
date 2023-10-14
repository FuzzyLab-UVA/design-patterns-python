from faker import Faker

fake = Faker()

class AddSpy:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.add_attribute = dict()

   
    def get_add(self):
        self.add_attribute['number1'] = self.a
        self.add_attribute['number2'] = self.b
        return fake.radom_number()