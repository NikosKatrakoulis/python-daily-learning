# Write a function called make_invitation() that has a default event_type
# of "birthday" and a default message of "You are invited!".
# The function should print a short description of the invitation.
# Call the function using only the default values.
# Call the function with a different event type but the default message.
# Call the function with both a different event type and a different message.

def make_invitation(event_type="birthday", message="You are invited!"):
    """Summarize the event that is going to be happened."""
    print(f"\nI'm going to make an invitation for my {event_type}.")
    print(f"It will say, '{message}'.")


make_invitation()
make_invitation(event_type="dinner")
make_invitation(event_type="name day",
                message="Come to my name day celebration at Alio")
