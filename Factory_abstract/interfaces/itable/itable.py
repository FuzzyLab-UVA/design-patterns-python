from abc import ABC, abstractmethod

class ITable(ABC):
    @abstractmethod
    def hasLegs(self):
        pass

    @abstractmethod
    def sitOn(self):
        pass