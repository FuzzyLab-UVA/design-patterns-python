from .default import Default
from ..Order import Order
from faker import Faker

fake = Faker()


def test_calculte():
    number =  fake.random_number()
    order = Order(number)
    default = Default()

    assert default.calculate(order) == number * 0.05
