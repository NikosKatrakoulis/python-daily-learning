class Employee:
    """A class representing an employee."""

    def __init__(self, first_name, last_name, employee_id, department):
        """Initialize attributes of employee."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.employee_id = employee_id
        self.department = department.title()

    def describe_employee(self):
        """Display a summary of employee."""
        print(f"\nName: {self.first_name} {self.last_name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
