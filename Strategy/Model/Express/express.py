from Interface import IShipping

class Express(IShipping):

    def calculate(self, order)-> float:
        return order.value * 0.1