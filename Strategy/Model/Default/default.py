from Interface import IShipping

class Default(IShipping):

    def calculate(self, order)-> float:
        return order.value * 0.05