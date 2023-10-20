from interfaces import IFurnitureFactory, IChair, ITable, ISofa
from models import MordernFurnitureChair, MordernFurnitureTable, MordernFurnitureSofa


class MordernFurnitureFactory(IFurnitureFactory):

    def create_chair(self) -> IChair:
        return MordernFurnitureChair()

    def create_table(self) -> ITable:
        return MordernFurnitureTable()

    def create_sofa(self) -> ISofa:
        return MordernFurnitureSofa()