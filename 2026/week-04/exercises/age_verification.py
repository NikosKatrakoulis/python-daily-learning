# Write a program that asks the user for their age. Convert the input to an
# integer and print a message saying whether the user is: under 18 or 18 and
# older. Catch the ValueError if the user enters non-numeric input and print
# a friendly error message.

try:
    age = int(input("How old are you?"))
except ValueError:
    print("Sorry, I really need a number.")
else:
    if age < 18:
        print(f"You are {age} years old. It is not eligible to vote.")
    else:
        print(f"You are {age} years old. You can vote!")
