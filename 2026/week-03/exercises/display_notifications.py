# Make a list containing several notification messages.
# Pass the list to a function called show_notifications(),
# which prints each notification message.

def show_notitications(notifications):
    """Print all notifications in the list."""
    for notification in notifications:
        print(notification)


notifications = ["A user looked your profile",
                 "Giorgos Papadopoulos sent you a friend request"]
show_notitications(notifications)
