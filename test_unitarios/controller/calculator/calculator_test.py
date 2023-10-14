from calculator import Calculator
from add import Add
from faker import Faker

fake = Faker()

def test_sum():
    number1 = fake.random_number()
    number2 = fake.random_number()
    calculadora = Calculator(number1,number2)
    sum = Add(number1,number2)

    assert calculadora.get_add() == sum.get_add()
