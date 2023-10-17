from interfaces import ISofa

class MordernFurnitureSofa(ISofa): 
    def hasLegs(self):
        return False
    
    def sitOn(self):
        return "Sitting on a morden sofa"
    