from abc import ABC, abstractmethod
from Model.Order import Order

class IShipping(ABC):
    @abstractmethod
    def calculate(self, order: Order) -> float:
        pass