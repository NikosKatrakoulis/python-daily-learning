# Create a module called employee.py. Inside this module, store the
# following classes: Employee (basic employee information) Manager
# (inherits from Employee) Responsibilities (stores a list of responsibilities)
# The Manager class should contain a Responsibilities instance as an attribute.
# Create a separate file called my_employee.py.
# Import the Manager class, create an instance, assign several
# responsibilities, and call a method to display them to confirm
# everything works correctly.

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


class Manager(Employee):
    """A class representing a manager."""

    def __init__(self, first_name, last_name, employee_id, department, location, resposibilities=[]):
        """Initialize the manager."""
        super().__init__(first_name, last_name, employee_id, department, location)
        self.responsibilities = resposibilities

    def show_responsibilities(self):
        """Print the responsibilities of the manager."""
        print("\nResponsibilities:")
        for responsibility in self.responsibilities:
            print(f"- {responsibility}")
