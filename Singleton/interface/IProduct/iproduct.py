from abc import ABC, abstractmethod

class IProduct(ABC):

    @property
    @abstractmethod
    def name(self)-> str:
        pass

    @property
    @abstractmethod
    def price(self)-> float:
        pass
