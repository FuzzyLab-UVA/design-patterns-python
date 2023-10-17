from .victorian_furniture_table import VictorianFurnitureTable


from interfaces import ITable

def test_victorian_furniture_table():
    table = VictorianFurnitureTable()
    
    assert table is not None
    assert table.hasLegs() == True
    assert table.sitOn() == False
    assert issubclass(VictorianFurnitureTable, ITable) == True