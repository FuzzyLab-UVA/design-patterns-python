from abc import ABC, abstractmethod

class IUser(ABC):

    @property
    @abstractmethod
    def name(self)-> str:
        pass

    @property
    @abstractmethod
    def login(self)-> str:
        pass

    @property
    @abstractmethod
    def password(self)-> str:
        pass