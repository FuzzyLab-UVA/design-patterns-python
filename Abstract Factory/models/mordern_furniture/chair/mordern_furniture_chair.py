from interfaces import IChair

class MordernFurnitureChair(IChair): 
    def hasLegs(self):
        return False
    
    def sitOn(self):
        return "Sitting on a morden chair"