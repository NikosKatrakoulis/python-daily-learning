# Create a list called notifications containing several short notification
# messages. Write a function called show_notifications() that prints each
# notification. Write a function called send_notifications() that prints
# each notification and moves it to a new list called sent_notifications.
# After calling the function, print both lists to confirm the notifications
# were moved correctly.

def show_notifications(notifications):
    """Print all notifications in the list"""
    for notification in notifications:
        print(notification)


def send_notifications(notifications, sent_notifications):
    """Print each notification and then move it to sent_notifications."""
    print("\nSending all notications:")
    while notifications:
        current_notification = notifications.pop()
        print(current_notification)
        sent_notifications.append(current_notification)


notifications = [
    "Giorgos sent you an iMessage.",
    "Father called you.",
    "Sofia liked your photo."
]
show_notifications(notifications)

sent_notifications = []
send_notifications(notifications, sent_notifications)

print("\nFinal lists:")
print(notifications)
print(sent_notifications)
