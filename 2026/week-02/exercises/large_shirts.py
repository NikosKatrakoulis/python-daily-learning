# Modify the make_shirt() function so that shirts are large by default
# with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with
# a different message.

def make_shirt(message='I love Python', size='large'):
    """Summarize the shirt that is going to be made."""
    print(f"\nI'm going to make a {size} shirt.")
    print(f"It will say, '{message}'")


make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='I love Sofaki')
