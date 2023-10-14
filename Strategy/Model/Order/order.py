class Order:
    def __init__(self,value):
        self.__value: float = value

    @property
    def value(self) -> float:
        return self.__value