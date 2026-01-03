# Each time you use the input() function, you should include a
# clear, easy-to-follow prompt that tells the user exactly what
# kind of information you’re looking for. Any statement that
# tells the user what to enter should work. For example:

name = input("Please enter you name:")
print(f"\nHello {name}!")

# Sometimes you’ll want to write a prompt that’s longer
# than one line. For example, you might want to tell the user
# why you’re asking for certain input. You can assign your
# prompt to a variable and pass that variable to the input()
# function. This allows you to build your prompt over several
# lines, then write a clean input() statement.
# This example shows one way to build a multiline string.
# The first line assigns the first part of the message to the
# variable prompt. In the second line, the operator += takes the
# string that was assigned to prompt and adds the new string
# onto the end.

prompt = "If you share your name, we can personalize the mess ages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello, {name}!")
