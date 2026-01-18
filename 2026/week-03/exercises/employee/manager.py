from employee import Employee as emp


class Manager(emp):
    """A class representing a manager."""

    def __init__(self, first_name, last_name, employee_id, department):
        """initialize the manager."""
        super().__init__(first_name, last_name, employee_id, department)
        self.responsibilities = Responsibilities()


class Responsibilities:
    """A class representing the responsibilities of a manager."""

    def __init__(self, responsibilities=[]):
        """Initialize the responsibilites."""
        self.responsibilities = responsibilities

    def show_responsibilities(self):
        """Display the responsibilities."""
        print("\nResponsibilities:")
        for responsibility in self.responsibilities:
            print(f"- {responsibility}")


manager = Manager('nikos', 'katrakoulis', 1234_5678_509, 'ai engineering')
manager.describe_employee()

manager_responsibilities = [
    "Organise the team",
    "Make tasks through the projects",
    "Resolve any upcoming problem in the team",
]

manager.responsibilities.responsibilities = manager_responsibilities
manager.responsibilities.show_responsibilities()
