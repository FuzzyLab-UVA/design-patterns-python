from .product import Product    
from faker import Faker

fake = Faker()

def test_product():
    name = fake.name()
    price = fake.pyfloat()
    product = Product(name,price)

    assert isinstance(product, Product) 
    assert product is not None
    assert product.name == name
    assert product.price == price

