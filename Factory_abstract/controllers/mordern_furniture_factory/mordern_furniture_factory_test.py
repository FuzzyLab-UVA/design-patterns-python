from interfaces import IFurnitureFactory, IChair, ITable, ISofa
from .mordern_furniture_factory import MordernFurnitureFactory

def test_mordern_furniture_factory():
    factory = MordernFurnitureFactory()
    chair = factory.create_chair()
    table = factory.create_table()
    sofa = factory.create_sofa()

    assert isinstance(chair, IChair)
    assert isinstance(table, ITable)
    assert isinstance(sofa, ISofa)
    assert isinstance(factory, IFurnitureFactory)