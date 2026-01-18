# Make a class called Spinner with one attribute called max_number, which
# has a default value of 8. Write a method called spin() that returns a
# random number between 1 and max_number. Make an 8-number spinner and
# spin it 10 times. Make a 12-number spinner and spin it 10 times.
# Make a 30-number spinner and spin it 10 times.
# Print the results for each spinner.

from random import randint


class Spinner:
    """Represent a spinner, which can be spinned."""

    def __init__(self, max_number=8):
        """Initialize the spinner."""
        self.max_number = max_number

    def spin(self):
        """Return a number between 1 and max_number."""
        return randint(1, self.max_number)


spinner = Spinner()

results = []
for spin_num in range(10):
    result = spinner.spin()
    results.append(result)
print("10 spins of a 8 numbered spin:")
print(results)

spinner = Spinner(max_number=12)

results = []
for spin_num in range(10):
    result = spinner.spin()
    results.append(result)
print("\n10 spins of a 12 numbered spin:")
print(results)

spinner = Spinner(max_number=30)

results = []
for spin_num in range(10):
    result = spinner.spin()
    results.append(result)
print("\n10 spins of a 30 numbered spin:")
print(results)
