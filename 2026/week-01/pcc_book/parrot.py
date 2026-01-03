# The input() function takes one argument: the prompt that
# we want to display to the user, so they know what kind of
# information to enter. In this example, when Python runs the
# first line, the user sees the prompt Tell me something, and I
# will repeat it back to you: . The program waits while the
# user enters their response and continues after the user
# presses ENTER. The response is assigned to the variable
# message, then print(message) displays the input back to the
# user:

message = input("Tell me something and I will repeat it back to you:")
print(message)

# We can make the parrot.py program run as long as the user
# wants by putting most of the program inside a while loop.
# We’ll define a quit value and then keep the program running
# as long as the user has not entered the quit value.

prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# This program works well, except that it prints the word
# 'quit' as if it were an actual message. A simple if test fixes
# this:

    if message != 'quit':
        print(message)

# Now the program makes a quick check before displaying
# the message and only prints the message if it does not
# match the quit value.

# For a program that should run only as long as many
# conditions are true, you can define one variable that
# determines whether or not the entire program is active. This
# variable, called a flag, acts as a signal to the program. We
# can write our programs so they run while the flag is set to
# True and stop running when any of several events sets the
# value of the flag to False. As a result, our overall while
# statement needs to check only one condition: whether the
# f
# lag is currently True. Then, all our other tests (to see if an
# event has occurred that should set the flag to False) can be
# neatly organized in the rest of the program.
# Let’s add a flag to parrot.py from the previous section.
# This flag, which we’ll call active (though you can call it
# anything), will monitor whether or not the program should
# continue running:

prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
