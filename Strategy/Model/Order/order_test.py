from .order import Order
from faker import Faker

fake = Faker()

def test_value():
    value = fake.random_number()
    order = Order(value)

    assert order.value == value