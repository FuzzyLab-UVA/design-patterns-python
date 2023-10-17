from interfaces import IChair

class VictorianFurnitureChair(IChair):
    def hasLegs(self):
        return True

    def sitOn(self):
        return "Sitting on a victorian chair"