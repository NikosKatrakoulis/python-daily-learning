# The upper() and lower() string methods return a new string with all the let
# ters in the original converted to uppercase or lowercase, respectively. Non
# letter characters in the string remain unchanged.

spam = 'Hello, World!'
print(spam.upper())
print(spam.lower())

# Note that these methods don’t change the string itself, but return new
# string values. If you want to change the original string, you have to call
# upper() or lower() on the string and then assign the new string to the vari
# able that stored the original.This is why you must use spam = spam.upper()
# to change the string in spam instead of simply writing spam.upper().

# spam = spam.upper()
# spam = spam.lower()

# The upper() and lower() methods are helpful if you need to make a case
# insensitive comparison. For example, the strings 'great' and 'GREat' aren’t
# equal to each other, but in the following small program, the user can enter
# Great, GREAT, or grEAT, because the code converts the string to lowercase:

print("How are you?")
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

# When you run this program, it displays a question, and entering any
# variation on great, such as GREat, will give the output I feel great too.
# Adding code to your program to handle variations or mistakes in user input,
# such as inconsistent capitalization, will make your programs easier to use
# and less likely to fail.
