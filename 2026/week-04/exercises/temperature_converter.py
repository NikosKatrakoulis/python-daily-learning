# Write a program that asks the user to enter a temperature in Celsius.
# Convert the value to Fahrenheit and print the result. Use a try-except
# block to catch invalid input and print a friendly error message if the
# input is not a number.

try:
    tempCels = float(input("Enter the temperature in Celsius:"))
except ValueError:
    print("Sorry, I really need a number.")
else:
    tempFah = tempCels * 9/5 + 32
    print(f"{tempCels} celsius is {tempFah} in fahrenheit.")
