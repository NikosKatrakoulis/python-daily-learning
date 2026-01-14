# Create a file called order_system.py.
# Import the functions from order_functions.py and use
# them to process a list of orders.

import order_functions as of

customer_orders = ["iPhone 16 Pro Max", "macBook Pro 16 Max", "iPad Pro 2022"]
completed_orders = []

of.show_customer_orders(customer_orders, completed_orders)
of.show_completed_orders(completed_orders)
