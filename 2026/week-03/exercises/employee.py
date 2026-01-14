# Make a class called Employee.
# Create attributes such as first_name, last_name, employee_id,
# department, and location. Add a method called describe_employee()
# that prints a summary of the employee’s information.
# Add a method called greet_employee() that prints a personalized greeting.
# Create several instances representing different employees, and
# call both methods for each employee.

class Employee:
    """Represent an employee."""

    def __init__(self, first_name, last_name, employee_id, department, location):
        """Initialize the employee."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.employee_id = employee_id
        self.department = department.title()
        self.location = location.title()

    def describe_employee(self):
        """Display the summary of the employee's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Location: {self.location}")

    def greet_employee(self):
        """Display a personalized greeting."""
        print(
            f"\nHello {self.first_name} {self.last_name}, welcome to the platform.")


employee1 = Employee('mpampis', 'papageorgiou', 12232779,
                     'management', 'thessaloniki')
employee1.describe_employee()
employee1.greet_employee()
