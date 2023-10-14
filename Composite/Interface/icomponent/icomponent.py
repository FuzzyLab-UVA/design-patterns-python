from abc import ABC, abstractmethod

class IComponent(ABC):

    @abstractmethod
    def get_size(self) -> float:
        pass