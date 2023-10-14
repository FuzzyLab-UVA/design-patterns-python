from Interface import IShipping
from Model.Order import Order

class Default(IShipping):

    def calculate(self, order)-> float:
        return order.value * 0.05