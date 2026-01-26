# Write a program that asks the user:
# “Do you want to continue? (yes/no)”

# Accept YES, Yes, yEs, etc. as “yes” using a case-insensitive check.
# If the answer is yes, print: “Continuing…”
# Otherwise print: “Goodbye!”

prompt = input("Do you want to continue? (yes/no)")
if prompt.lower() == 'yes':
    print("Continuing...")
else:
    print("Goodbye!")
