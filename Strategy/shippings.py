class Default(object):

    def calculate(self, order):
        return order.value * 0.05


class Express(object):

    def calculate(self, order):
        return order.value * 0.1