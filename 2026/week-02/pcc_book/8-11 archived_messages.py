# Archived Messages: Start with your work from Exercise 8-10. Call
# the function send_messages() with a copy of the list of messages. After calling
# the function, print both of your lists to show that the original list has
# retained its messages.

def show_messages(messages):
    print("Showing all messages:")
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    print("Sending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = ['Hello World', 'My name is Nikos', 'I like to dance']
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
