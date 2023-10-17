from .victorian_furniture_chair import VictorianFurnitureChair
from interfaces import IChair

def test_victorian_furniture_chair():
    chair = VictorianFurnitureChair()
    
    assert chair is not None
    assert chair.hasLegs() == True
    assert chair.sitOn() == "Sitting on a victorian chair"
    assert issubclass(VictorianFurnitureChair, IChair) == True