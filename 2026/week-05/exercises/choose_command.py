# Write a program that asks the user to type a command:
# “Type START to begin or STOP to end.”

# Make the program accept any capitalization of start or stop.
# If the user types start → print: “Program started.”
# If the user types stop → print: “Program ended.”
# Otherwise print: “Unknown command.”

command = input("Type START to begin or STOP to end.")
if command.upper() == 'START':
    print("Program started.")
elif command.upper() == 'STOP':
    print("Program ended.")
else:
    print("Unknown command.")
