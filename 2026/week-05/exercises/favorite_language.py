# Write a program that asks the user:
# “What is your favorite programming language?”

# If the user types Python (in any capitalization), print a message like:
# “I like Python too!”
# Otherwise print:
# “Nice choice!”


answer = input("What is your favorite programming language?")
if answer.title() == 'Python':
    print("I like Python too!")
else:
    print("Nice choice!")
