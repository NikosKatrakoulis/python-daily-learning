# Write a program that repeatedly asks the user for their age.
# Convert the input to an integer.
# Print whether the user is a minor or an adult.
# Use a while loop so the user can retry after mistakes.
# Allow the user to quit by entering 'q'.
# Handle invalid input using try-except.

print("Enter 'q' at any time to quit.")

while True:
    try:
        age = input("How old are you?")
        if age == 'q':
            break

        age = int(age)
    except ValueError:
        print("Sorry, I really need a number.")
    else:
        if age < 18:
            print(f"You are {age} years old so you are a minor.")
        else:
            print(f"You are {age} years old so you are an adult.")
