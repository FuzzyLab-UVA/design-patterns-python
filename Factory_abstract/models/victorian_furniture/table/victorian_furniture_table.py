from interfaces import ITable

class VictorianFurnitureTable(ITable):
    def hasLegs(self):
        return True

    def sitOn(self):
        return False