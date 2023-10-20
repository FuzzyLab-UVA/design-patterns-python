from interface import IOwner, IUser, IProduct
from Product import Product

class Owner(IOwner,IUser):
    def __init__(self, name, login, password):
        self.__name = name
        self.__login = login
        self.__password = password

    @property
    def name(self):
        return self.__name

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password
    
    def create_product(self) -> IProduct:
        return Product("Lorem Impsum",33.5)