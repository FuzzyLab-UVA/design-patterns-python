from abc import ABC, abstractmethod

from ichair import IChair
from isofa import ISofa
from itable import ITable

class IFurnitureFactory(ABC):
    
    @abstractmethod
    def create_chair(self) -> IChair:
        pass

    @abstractmethod
    def create_table(self) -> ITable:
        pass

    @abstractmethod
    def create_sofa(self) -> ISofa:
        pass