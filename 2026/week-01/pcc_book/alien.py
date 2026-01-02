# Consider a game featuring aliens that can have different
# colors and point values. This simple dictionary stores
# information about a particular alien.

alien_0 = {'color': 'green', 'points': 5}


# To get the value associated with a key, give the name of the
# dictionary and then place the key inside a set of square
# brackets, as shown here:

print(alien_0['color'])
print(alien_0['points'])

# Now you can access either the color or the point value of
# alien_0. If a player shoots down this alien, you can look up
# how many points they should earn using code like this:

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Let’s add two new pieces of information to the alien_0
# dictionary: the alien’s x- and y-coordinates, which will help
# us display the alien at a particular position on the screen.

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# It’s sometimes convenient, or even necessary, to start with
# an empty dictionary and then add each new item to it. To
# start filling an empty dictionary, define a dictionary with an
# empty set of braces and then add each key-value pair on its
# own line. For example, here’s how to build the alien_0
# dictionary using this approach:

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Typically, you’ll use empty dictionaries when storing user
# supplied data in a dictionary or when writing code that
# generates a large number of key-value pairs automatically.

# To modify a value in a dictionary, give the name of the
# dictionary with the key in square brackets and then the new
# value you want associated with that key. For example,
# consider an alien that changes from green to yellow as a
# game progresses:

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']} .")

# For a more interesting example, let’s track the position of
# an alien that can move at different speeds. We’ll store a
# value representing the alien’s current speed and then use it
# to determine how far to the right the alien should move:

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"The original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] += x_increment

print(f"New position: {alien_0['x_position']}")


# When you no longer need a piece of information that’s
# stored in a dictionary, you can use the del statement to
# completely remove a key-value pair. All del needs is the
# name of the dictionary and the key that you want to
# remove. Be aware that the deleted key-value pair is removed
# permanently

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

print("\n")

# The alien_0 dictionary contains a variety of information
# about one alien, but it has no room to store information
# about a second alien, much less a screen full of aliens. How
# can you manage a fleet of aliens? One way is to make a list
# of aliens in which each alien is a dictionary of information
# about that alien. For example, the following code builds a
# list of three aliens:

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("\n")

# A more realistic example would involve more than three
# aliens with code that automatically generates each alien. In
# the following example, we use range() to create a fleet of 30
# aliens:

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# When it’s time to change colors, we can use a for loop and
# an if statement to change the color of the aliens. For
# example, to change the first three aliens to yellow, medium
# speed aliens worth 10 points each, we could do this:

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")
