# Create a module called employee.py. Inside this module, store the
# following classes: Employee (basic employee information) Manager
# (inherits from Employee) Responsibilities (stores a list of responsibilities)
# The Manager class should contain a Responsibilities instance as an attribute.
# Create a separate file called my_employee.py.
# Import the Manager class, create an instance, assign several
# responsibilities, and call a method to display them to confirm
# everything works correctly.

from employeee import Manager

nikos = Manager('nikos', 'katrakoulis', 1234_5667_54,
                'ai engineering', 'zurich')
nikos.describe_employee()
nikos.responsibilities = [
    "make a daily report",
    "organise the team for the daily tasks",
    "contact with the clients",
]

nikos.show_responsibilities()
