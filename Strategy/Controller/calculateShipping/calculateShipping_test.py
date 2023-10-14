from faker import Faker
from Test import CalculateShippingSpy
from Model.Order import Order
from Model.Default import Default

fake = Faker()

def test_execute_calculate():
    calculateShippingSpy = CalculateShippingSpy()
    order = Order(fake.random_number())   
    shipping = Default()
    calculateShippingSpy.execute_calculation(order, shipping)

    assert calculateShippingSpy.entry != {}
    assert calculateShippingSpy.execute_calculation(order, shipping) != None
    
    