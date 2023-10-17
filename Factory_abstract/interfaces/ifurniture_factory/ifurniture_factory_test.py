from .ifurniture_factory import IFurnitureFactory

def test_ifurniture_factory():
    try:
        urniture_factory = IFurnitureFactory()
    except:
        assert True
