from abc import ABC, abstractmethod
from ..iproduct import IProduct

class IOwner(ABC):
    @abstractmethod
    def create_product(self)-> IProduct:
        pass