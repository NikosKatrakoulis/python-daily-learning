# Write a function called full_name() that takes in a first name and a
# last name. The function should return a string formatted like this:
# "John Doe". Call the function with at least three name pairs, and print
# the returned values.

def full_name(first_name, last_name):
    """Return a string."""
    return f"\n{first_name.title()} {last_name.title()}"


name = full_name("nikos", "katrakoulis")
print(name)
name = full_name("sofia", "loukisa")
print(name)
name = full_name("giorgos", "papadopoulos")
print(name)
