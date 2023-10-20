from interfaces import ITable

class MordernFurnitureTable(ITable):
    
    def hasLegs(self):
        return False
    
    def sitOn(self):
        return False
