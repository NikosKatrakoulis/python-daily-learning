# Make a class called School.
# The __init__() method should store two attributes: school_name and location.
# Add a method called describe_school() that prints the school’s name and
# location. Add a method called open_school() that prints a message
# indicating the school is open.
# Create an instance of School.
# Print both attributes individually, and then call both methods.

class School:
    """A class representing a school."""

    def __init__(self, school_name, location):
        self.school_name = school_name.title()
        self.location = location.title()

    def describe_school(self):
        """Display a summary of a school."""
        msg = f"{self.school_name}'s location is in {self.location}."
        print(f"\n{msg}")

    def open_school(self):
        """Display that the school is open."""
        msg = f"{self.school_name} is now open. Come on in!"
        print(f"\n{msg}")


school = School('athens tech', 'ampelokipoi')
print(school.school_name)
print(school.location)

school.describe_school()
school.open_school()
