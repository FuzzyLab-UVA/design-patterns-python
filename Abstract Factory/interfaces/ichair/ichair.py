from abc import ABC, abstractmethod

class IChair(ABC):
    @abstractmethod
    def hasLegs(self):
        pass

    @abstractmethod
    def sitOn(self):
        pass