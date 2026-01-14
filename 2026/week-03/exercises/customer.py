# Make a class called Customer.
# Create attributes such as first_name, last_name, customer_id, email,
# and city. Add a method called describe_customer() that prints a summary
# of the customer’s information. Add a method called greet_customer()
# that prints a personalized greeting. Create at least two instances
# representing different customers, and call both methods for each one.

class Customer:
    """Represent a customer."""

    def __init__(self, first_name, last_name, customer_id, email, city):
        """Initialize the customer."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.customer_id = customer_id
        self.email = email
        self.city = city.title()

    def describe_customer(self):
        """Display a summary of the customer's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Email: {self.email}")
        print(f"City: {self.city}")

    def greet_customer(self):
        """Print a personalized greeting."""
        print(
            f"\nHello {self.first_name} {self.last_name}, welcome to the community!")


customer01 = Customer('Sofia', 'loukisa', '231234',
                      'solouj@example.com', 'meganisi')
customer01.describe_customer()
customer01.greet_customer()

customer02 = Customer('giorgos', 'papaggelis', '11223456',
                      'papagio@example.com', 'pirgos')
customer02.describe_customer()
customer02.greet_customer()

customer03 = Customer('stathis', 'papaefthimiou', '1929789',
                      'papastathis@example.com', 'methana')
customer03.describe_customer()
customer03.greet_customer()
