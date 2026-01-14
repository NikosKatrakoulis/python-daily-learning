# Create a file called message_functions.py that contains functions for
# sending messages. One function should send messages by moving them
# from a pending list to a sent list. Another function should display
# all sent messages.

def show_unsended_messages(unsended_messages, sent_messages):
    """Print the messages that need to be sent and move each to sent_messages."""
    while unsended_messages:
        current_message = unsended_messages.pop(0)
        print(f"Printing the sending message: {current_message}")
        sent_messages.append(current_message)


def show_sent_messages(sent_messages):
    """Display all the sent messages."""
    print("\nThe following messages have been sent:")
    for message in sent_messages:
        print(f"- {message}")
