# Using keys in square brackets to retrieve the value you’re
# interested in from a dictionary might cause one potential
# problem: if the key you ask for doesn’t exist, you’ll get an
# error.

""" alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points']) """

# You can use the get() method to set a default value that will be
# returned if the requested key doesn’t exist.
# The get() method requires a key as a first argument. As a
# second optional argument, you can pass the value to be
# returned if the key doesn’t exist:

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
