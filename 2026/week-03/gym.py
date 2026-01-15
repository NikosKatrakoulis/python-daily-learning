# Make a class called Gym. Add two constant attributes: gym_name, location
# Add one attribute with a default value: members_checked_in (default value: 0)
# Create an instance and print all attributes. Modify the value of
# members_checked_in directly and print it again. Add a method called
# set_members_checked_in() that sets the number of members who have checked in.
# Add a method called increment_members_checked_in() that increments
# this number by a given amount. Call both methods with realistic
# values and print the updated totals.

class Gym:
    """A class respresenting a gym."""

    def __init__(self, gym_name, location):
        """Initialize the gym."""
        self.gym_name = gym_name.title()
        self.location = location.title()
        self.members_checked = 0

    def describe_gym(self):
        """Display a summary of the gym."""
        msg = f"{self.gym_name} is a the best gym in {self.location}."
        print(f"\n{msg}")

    def open_gym(self):
        """Display a message that the gym is open."""
        msg = f"{self.gym_name} is now open. Come on in!"
        print(f"\n{msg}")

    def set_members_checked_in(self, members_checked_in):
        """Allow the user to set the checked in members."""
        self.members_checked = members_checked_in

    def inrement_members_checked_in(self, additional_members):
        """Allow the user to increase the checked in members."""
        self.members_checked += additional_members


gym = Gym('ultra flex', 'peristeri')
gym.describe_gym()
gym.open_gym()

print(f"Number of checked in members: {gym.members_checked}")
gym.members_checked = 153
print(f"Number of checked in members: {gym.members_checked}")

gym.set_members_checked_in(2003)
print(f"Number of checked in members: {gym.members_checked}")

gym.inrement_members_checked_in(15233)
print(f"Number of checked in members: {gym.members_checked}")
