# Write a program that asks the user to enter a secret word.
# If the user enters OpenSesame in any combination of
# uppercase/lowercase letters, print:
# “Access granted!”
# Otherwise print:
# “Access denied!”

word = input("Enter the secret word.")
if word.lower() == 'OpenSesame':
    print("Access granted!")
else:
    print("Access denied!")
