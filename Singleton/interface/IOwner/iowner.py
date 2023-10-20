from abc import ABC, abstractmethod
from IProduct import IProduct

class IOwner(ABC):
    @abstractmethod
    def create_product()-> IProduct:
        pass