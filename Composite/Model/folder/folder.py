from Interface import IComponent

class Folder(IComponent):
    
    def __init__(self, name, components):
        self._name:str = name
        self._components:list = components
        
    def get_size(self) -> float:
        total_size = 0
        for c in self._components:
            total_size += c.get_size()
        return total_size