class Order:
    def __init__(self,value):
        self.__value = value

    @property
    def value(self):
        return self.__value