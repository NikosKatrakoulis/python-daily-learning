# Make a list that contains 10 numbers and 5 special symbols
# (for example: @, #, $, %, &). Randomly select 4 unique items to create a
# lucky draw combination. Print a message saying that any ticket matching
# the 4 selected items wins a prize.
# Print the final lucky combination.

from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, '@', '#', '$', '%', '&']

lucky_combination = []
print("Let's see what is the lucky combination which wins the prize:")

while len(lucky_combination) < 4:
    pulled_item = choice(possibilities)

    if pulled_item not in lucky_combination:
        print(f"    We pulled a {pulled_item}")
        lucky_combination.append(pulled_item)

print(f"The final lucky combination which wins the price is:")
print(lucky_combination)
