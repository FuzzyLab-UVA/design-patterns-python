from Interface import IShipping

class Default(IShipping):

    def calculate(self, order):
        return order.value * 0.05