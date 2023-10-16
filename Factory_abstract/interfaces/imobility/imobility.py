from abc import ABC, abstractmethod

class IMobility(ABC):
    @abstractmethod
    def hasLegs(self):
        pass

    @abstractmethod
    def sitOn(self):
        pass