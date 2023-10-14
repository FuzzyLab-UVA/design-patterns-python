from Interface import IComponent

class File(IComponent):
    
    def __init__(self, name, size):
        self._name: str = name
        self._size: float = size
    
    def get_size(self)-> float:
        return self._size