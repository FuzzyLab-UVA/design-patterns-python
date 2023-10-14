from add import Add
from faker import Faker

fake = Faker()

def test_sum():

    number1 = fake.random_number()
    number2 = fake.random_number()
    expect = number1 + number2
    sum = Add(number1, number2)
    print(f"O resultado esperado era {expect}")
    print(f"O resultado final foi {sum.get_add()}")

    
    assert sum.get_add() == expect
