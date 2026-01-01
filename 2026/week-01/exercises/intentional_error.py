# Intentional Error: If you haven’t received an index error
# in one of your programs yet, try to make one happen.
# Change an index in one of your programs to produce an index error.
# Make sure you correct the error before closing the program.

places = ['Greece', 'Italy', 'Spain', 'Switzerland']

# Intentional error
# print(places[5])

# Correct access
print(places[3])


# Pro way to ensure that there will not be an error.
index = 5
if index < len(places):
    print(places[index])
