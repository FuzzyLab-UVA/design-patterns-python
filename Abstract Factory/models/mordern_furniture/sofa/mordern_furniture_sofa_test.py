from .mordern_furniture_sofa import MordernFurnitureSofa  
from interfaces import ISofa

def test_mordern_furniture_sofa():
    sofa = MordernFurnitureSofa()
    assert sofa.sitOn() == "Sitting on a morden sofa"
    assert sofa.hasLegs() == False
    assert isinstance(sofa, ISofa)