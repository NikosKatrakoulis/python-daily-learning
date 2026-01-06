# Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a
# different message.

def make_shirt(size='L', message='I love Python'):
    print(
        f"The shirt size is {size} and the message print on it is {message}.")


make_shirt()
make_shirt(size='M')
make_shirt(size='S', message='I love Sofaki')
