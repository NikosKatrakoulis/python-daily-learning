# A bus company charges different prices depending on age.
# Under 5 → free
# From 5 to 17 → $5
# 18 or older → $10
# Write a loop that asks for age and prints the ticket price.

while True:
    age = input("Enter your age(type 'quit' to stop):")

    if age == 'quit':
        break

    age = int(age)

    if age < 5:
        print("The ride is free.")
    elif age < 18:
        print("Your ticket costs $5.")
    else:
        print("Your ticket costs $10.")
