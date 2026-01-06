# When you pass a list to a function, the function can modify
# the list. Any changes made to the list inside the function’s
# body are permanent, allowing you to work efficiently even
# when you’re dealing with large amounts of data.
# Consider a company that creates 3D printed models of
# designs that users submit. Designs that need to be printed
# are stored in a list, and after being printed they’re moved to
# a separate list. The following code does this without using
# functions:

# Start with some desings that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


# We can reorganize this code by writing two functions,
# each of which does one specific job. Most of the code won’t
# change; we’re just structuring it more carefully. The first
# function will handle printing the designs, and the second will
# summarize the prints that have been made:

def print_models(unprinted_desings, completed_models):
    """
    Simulate printing each designm until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_desings.pop()
        print(f"Printing model: {current_design}!")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# This program has the same output as the version without
# functions, but the code is much more organized. The code
# that does most of the work has been moved to two separate
# functions, which makes the main part of the program easier
# to understand.

# Sometimes you’ll want to prevent a function from modifying
# a list. you want to keep the original list of unprinted designs for your
# records. But because you moved all the design names out of
# unprinted_designs, the list is now empty, and the empty list is
# the only version you have; the original is gone. In this case,
# you can address this issue by passing the function a copy of
# the list, not the original.
# The slice notation [:] makes a copy of the list to send to
# the function. If we didn’t want to empty the list of unprinted
# designs in printing_models.py, we could call print_models()
# like this:

# print_models(unprinted_designs[:], completed_models)
