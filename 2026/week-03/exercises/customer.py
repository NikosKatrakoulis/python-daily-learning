# Make a class called Customer.
# Create attributes such as first_name, last_name, customer_id, email,
# and city. Add a method called describe_customer() that prints a summary
# of the customer’s information. Add a method called greet_customer()
# that prints a personalized greeting. Create at least two instances
# representing different customers, and call both methods for each one.

class Customer:
    """Represent a customer."""

    def __init__(self, first_name, last_name, customer_id, email, city):
        self.first_name = first_name.title()
