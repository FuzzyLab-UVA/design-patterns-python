from add import Add
from subt import Subt

class Calculator:
    def __init__(self,a,b) -> None:
        self.add = Subt(a,b)
        self.add = Add(a,b)

    def get_add(self):
        return self.add.get_add()
    
    def get_sub(self):
        return self.sub.get_subt()