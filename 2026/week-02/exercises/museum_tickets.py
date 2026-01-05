# A museum charges different ticket prices based on age.
# If a person is under 6, the ticket is free; if they are
# between 6 and 17, the ticket is $8; and if they are 18 or
# older, the ticket is $12. Write a loop that asks users their
# age and then tells them the cost of their ticket. Let the
# user type quit to stop.

while True:
    age = input("Enter your age:(type 'quit' to stop)")

    if age == 'quit':
        break

    age = int(age)

    if age < 6:
        print("The ticket is free.")
    elif age < 17:
        print("The ticket costs $8.")
    else:
        print("The ticket costs $12.")
