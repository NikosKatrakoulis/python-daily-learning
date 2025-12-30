alien_0 = {'color': 'green', 'points': 5}

# To get the value associated with a key, give the name of the
# dictionary and then place the key inside a set of square
# brackets.
print(alien_0['color'])
print(alien_0['points'])

# Now you can access either the color or the point value of
# alien_0. If a player shoots down this alien, you can look up
# how many points they should earn using code like this:
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x position'] = 0
alien_0['y position'] = 25

print(alien_0)

alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

alien_0 = {'color': 'green'}

print(f"The alien is {alien_0['color']}!")

alien_0['color'] = 'yellow'

print(f"The alien is now {alien_0['color']} color!")

print("\n\n\n\n\n\n")

alien_0 = {'x position': 0, 'y position': 25, 'speed': 'medium'}

print(f"The original position: {alien_0['x position']}")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x position'] = alien_0['x position'] + x_increment

print(f"The new x-position: {alien_0['x position']}")
