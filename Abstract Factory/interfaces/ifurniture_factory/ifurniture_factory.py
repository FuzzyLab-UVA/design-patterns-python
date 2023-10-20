from abc import ABC, abstractmethod

from ..ichair import IChair
from ..itable import ITable
from ..isofa import ISofa

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