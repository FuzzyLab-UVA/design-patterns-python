from .mordern_furniture_chair import MordernFurnitureChair

from interfaces import IChair

def test_morden_furniture_chair():
    chair = MordernFurnitureChair()

    assert chair.hasLegs() == False
    assert chair.sitOn() == "Sitting on a morden chair"
    assert issubclass(MordernFurnitureChair, IChair) == True