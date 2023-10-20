from abc import ABC, abstractmethod

class ISofa(ABC):
    @abstractmethod
    def hasLegs(self):
        pass

    @abstractmethod
    def sitOn(self):
        pass