from interfaces import ISofa

class VictorianFurnitureSofa(ISofa):
    def hasLegs(self):
        return False

    def sitOn(self):
        return "Sitting on a victorian sofa"