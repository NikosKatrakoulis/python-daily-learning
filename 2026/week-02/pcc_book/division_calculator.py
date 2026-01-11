# When you think an error may occur, you can write a try
# except block to handle the exception that might be raised.
# You tell Python to try running some code, and you tell it
# what to do if the code results in a particular kind of
# exception.
# Here’s what a try-except block for handling the
# ZeroDivisionError exception looks like:

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# When you think an error may occur, you can write a try
# except block to handle the exception that might be raised.
# You tell Python to try running some code, and you tell it
# what to do if the code results in a particular kind of
# exception.
# Here’s what a try-except block for handling the
# ZeroDivisionError exception looks like.

# Handling errors correctly is especially important when the
# program has more work to do after the error occurs. This
# happens often in programs that prompt users for input. If
# the program responds to invalid input appropriately, it can
# prompt for more valid input instead of crashing.
# Let’s create a simple calculator that does only division:


"""

print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

"""

# We can make this program more error resistant by wrapping
# the line that might produce errors in a try-except block. The
# error occurs on the line that performs the division, so that’s
# where we’ll put the try-except block. This example also
# includes an else block. Any code that depends on the try
# block executing successfully goes in the else block:

print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# We ask Python to try to complete the division operation in
# a try block, which includes only the code that might cause
# an error. Any code that depends on the try block succeeding
# is added to the else block. In this case, if the division
# operation is successful, we use the else block to print the
# result.
