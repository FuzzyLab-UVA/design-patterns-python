class CalculateShipping(object):

    def execute_calculation(self, order, shipping):
        total = shipping.calculate(order)
        
        return total