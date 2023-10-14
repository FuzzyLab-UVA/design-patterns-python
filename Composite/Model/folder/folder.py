from Interface import IComponent

class Folder(IComponent):
    
    def __init__(self, name, components):
        self._name = name
        self._components = components
        
    def get_size(self):
        total_size = 0
        for c in self._components:
            total_size += c.get_size()
        return total_size