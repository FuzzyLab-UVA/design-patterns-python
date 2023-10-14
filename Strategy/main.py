from order import Order
from calculateShipping import CalculateShipping
from shippings import Default, Express

order = Order(500)
calculate_shipping = CalculateShipping()

calculate_shipping.execute_calculation(order,Default())