from interfaces import IFurnitureFactory, IChair, ISofa ,ITable
from models import VictorianFurnitureChair, VictorianFurnitureSofa, VictorianFurnitureTable

class VictorianFurnitureFactory(IFurnitureFactory):
    
    def create_chair(self) -> IChair:
        return VictorianFurnitureChair()
    
    def create_sofa(self) -> ISofa:
        return VictorianFurnitureSofa()
    
    def create_table(self) -> ITable:
        return VictorianFurnitureTable()

