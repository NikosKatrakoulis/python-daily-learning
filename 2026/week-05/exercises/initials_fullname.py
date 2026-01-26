# Ask the user for a full name (example: "Nikos Katrakoulis").
# Use split() to break it into parts, then build the initials
# (example: "N.K.") using join().

full_name = input("What's your name?")

parts = full_name.split()

initials = [name[0].upper()for name in parts]

result = '.'.join(initials) + '.'

print(result)
