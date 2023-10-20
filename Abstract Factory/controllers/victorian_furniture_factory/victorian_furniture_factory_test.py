from .victorian_furniture_factory import VictorianFurnitureFactory
from interfaces import IFurnitureFactory, IChair, ISofa ,ITable

def test_victorian_furniture_factory():
    factory = VictorianFurnitureFactory()

    assert isinstance(factory.create_chair(), IChair) == True   
    assert isinstance(factory.create_sofa(), ISofa) == True
    assert isinstance(factory.create_table(), ITable) == True
    assert issubclass(VictorianFurnitureFactory, IFurnitureFactory) == True