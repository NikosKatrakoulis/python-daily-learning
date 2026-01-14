# Make a class called Student.
# Create attributes such as first_name, last_name, student_id, major,
# and year. Add a method called describe_student() that prints a summary
# of the student’s information. Add a method called greet_student()
# that prints a personalized message to the student. Create multiple
# instances representing different students, and call both methods for
# each one.

class Student:
    """Represent the student."""

    def __init__(self, first_name, last_name, student_id, major, year):
        """Initialize the student."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.student_id = student_id
        self.major = major.title()
        self.year = year

    def describe_student(self):
        """Display a summary of the student's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Student ID: {self.last_name}")
        print(f"Major: {self.major}")
        print(f"Year: {self.year}")

    def greet_student(self):
        """Display a personalized message."""
        print(
            f"\nHello {self.first_name} {self.last_name}, welcome to iLearn.")


student01 = Student('nikos', 'katrakoulis', 1233444,
                    'software development', '3rd Bachelor')
student01.describe_student()
student01.greet_student()

student02 = Student('anastasia', 'mpakopoulou', 98900763,
                    'data science', '2nd Master')
student02.describe_student()
student02.greet_student()

student03 = Student('christos', 'papalexiou', 723451,
                    'civil engineering', '1rst Bachelor')
student03.describe_student()
student03.greet_student()
