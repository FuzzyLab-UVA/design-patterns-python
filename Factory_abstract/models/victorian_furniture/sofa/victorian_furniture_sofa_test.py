from .victorian_furniture_sofa import VictorianFurnitureSofa
from interfaces import ISofa

def test_victorian_furniture_sofa():
    sofa = VictorianFurnitureSofa()
    
    assert sofa is not None
    assert sofa.hasLegs() == False
    assert sofa.sitOn() == "Sitting on a victorian sofa"
    assert issubclass(VictorianFurnitureSofa, ISofa) == True