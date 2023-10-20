from models.owner import Owner
from interface import IOwner

class SingletonOwner:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(SingletonOwner, cls).__new__(cls)
            cls._instance.init_owner()
        return cls._instance

    def init_owner(self) -> None:
        from models.owner import Owner
        self.owner = Owner("Paulo Ricardo", "paulitos", 'pqvcquersaber?')

    def get_owner(self) -> Owner:
        return self.owner
