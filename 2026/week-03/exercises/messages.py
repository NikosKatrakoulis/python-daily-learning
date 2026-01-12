# Make a list containing a series of short text messages.
# Pass the list to a function called show_messages(), which
# prints each text message.


def show_messages(messages):
    """Print all messages in the list."""
    for message in messages:
        print(message)


messages = ["Hey there", "How are you doing?"]
show_messages(messages)
