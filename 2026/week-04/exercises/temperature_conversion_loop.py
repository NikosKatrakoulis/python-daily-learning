# Write a program that repeatedly asks the user to enter a temperature in
# Celsius and converts it to Fahrenheit. Wrap the program in a while loop.
# Allow the user to quit by entering 'q'. Use try-except to handle invalid
# input. Print a clear error message if the input is not a number.

print("Enter 'q' at any time to quit.")

while True:
    try:
        tempCels = input("What is the temperature in Celsius?")
        if tempCels == 'q':
            break

        tempCels = int(tempCels)
    except ValueError:
        print("Sorry I really need a number.")
    else:
        tempFahren = tempCels * 9/5 + 32
        print(f"{tempCels} Celsius are {tempFahren} Fahrenheit.")
