from Interface import IShipping

class Express(IShipping):

    def calculate(self, order):
        return order.value * 0.1