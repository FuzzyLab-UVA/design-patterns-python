from abc import ABC, abstractmethod

class IShipping(ABC):
    @abstractmethod
    def calculate(self, order):
        pass