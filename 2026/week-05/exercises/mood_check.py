# Write a program that asks the user:
# “How do you feel today? (happy/sad)”

# Make the comparison case-insensitive.
# If the user enters “happy”, print a positive message.
# If the user enters “sad”, print a supportive message.
# If they enter something else, print: “Thanks for sharing!”

feeling = input("How do you feel today? (happy/sad)")
if feeling.lower() == 'happy':
    print("Enjoy your great day!")
elif feeling.lower() == 'sad':
    print("Hope you will enjoy your day!")
else:
    print("Thanks for sharing!")
