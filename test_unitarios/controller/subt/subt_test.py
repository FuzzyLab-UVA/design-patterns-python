from subt import Subt
from faker import Faker

fake = Faker()

def test_sub():
    number1 = fake.random_number()
    number2 = fake.random_number()
    expect = number1 - number2

    sub = Subt(number1, number2)
    assert sub.get_subt() == expect
