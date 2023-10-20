from interface import IOwner, IProduct
from .owner import Owner
from faker import Faker

fake = Faker()


def test_owner():
    name =  fake.name()
    login = fake.email()
    password = fake.password()
    owner = Owner(name, login, password)

    assert owner is not None
    assert isinstance(owner, IOwner)
    assert owner.name == name
    assert owner.login == login
    assert owner.password == password
    assert isinstance(owner.create_product(), IProduct)
