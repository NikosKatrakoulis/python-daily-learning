# Create a file called message_app.py.
# Import the functions from message_functions.py and use
# them to send and display messages.

import message_functions as mf

unsended_messages = ["Goodmorning Sofaki mou",
                     "How are you doing?", ":)", "I'm on the way to pick you up"]
sent_messages = []

mf.show_unsended_messages(unsended_messages, sent_messages)
mf.show_sent_messages(sent_messages)
