# Make a list containing 12 numbers and 8 letters.
# Randomly select 5 unique items from the list to create a coupon code.
# Print a message saying that any coupon code matching these 5 items wins
# a discount. Print the final coupon code.

from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 11, 12, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
