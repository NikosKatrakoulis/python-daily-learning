# Create a file called order_functions.py that contains functions for
# processing customer orders. One function should process pending orders
# and move them to a completed orders list. Another function should
# display all completed orders.


def show_customer_orders(customer_orders, completed_orders):
    """Display each customer order and move it to completed_order."""
    while customer_orders:
        current_order = customer_orders.pop()
        print(
            f"I'll check your order about the {current_order} you want to buy.")
        completed_orders.append(current_order)


def show_completed_orders(completed_orders):
    """Print out all the completed orders."""
    print("\nThe completed orders:")
    for order in completed_orders:
        print(f"- {order}")
