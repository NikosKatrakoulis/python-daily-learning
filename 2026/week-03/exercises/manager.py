# A manager is a special type of employee. Create a class called
# Employee with basic attributes such as first_name, last_name,
# and department. Then create a class called Manager that inherits
# from Employee. Add an attribute called responsibilities that stores
# a list of responsibilities (for example: "approve budget", "assign tasks",
# "review performance"). Write a method called show_responsibilities()
# that prints all responsibilities. Create an instance of Manager,
# add at least three responsibilities, and call the method.

class Employee:
    """A class representing an employee's profile."""

    def __init__(self, first_name, last_name, department):
        """Initialize the employee."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.department = department.title()

    def describe_employee(self):
        """Display a summary of the employee."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Department: {self.department}")


class Manager(Employee):
    """An employee with responsibilities."""

    def __init__(self, first_name, last_name, department):
        """initialize the employee."""
        super().__init__(first_name, last_name, department)
        self.responsibilities = []

    def show_responsibilities(self):
        """Display the responsibilities this manager has."""
        print("\nResponsibilities:")
        for responsibility in self.responsibilities:
            print(f"- {responsibility}")


manager = Manager('giorgos', 'papadopoulos', 'ai engineering')
manager.describe_employee()

manager.responsibilities = [
    "approve budget",
    "assign tasks",
    "review performance",
]

manager.show_responsibilities()
