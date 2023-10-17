from .mordern_furniture_table import MordernFurnitureTable
from interfaces import ITable

def test_morden_funiture_table():
    table = MordernFurnitureTable()

    assert table.hasLegs() == False
    assert table.sitOn() == False
    assert issubclass(MordernFurnitureTable, ITable)