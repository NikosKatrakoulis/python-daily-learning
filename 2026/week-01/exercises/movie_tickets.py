# Write a program that repeatedly asks the user for their age.
# If the user enters quit, the program should stop.
# If the age is under 3, the ticket is free.
# If the age is between 3 and 12, the ticket costs $10.
# If the age is over 12, the ticket costs $15.
# After each entry, display the ticket price.


active = True
while True:
    age = input("Enter your age (type 'quit' to finish):")

    if age == 'quit':
        active = False
