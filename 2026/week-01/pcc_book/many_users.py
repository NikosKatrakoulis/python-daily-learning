# You can nest a dictionary inside another dictionary, but your
# code can get complicated quickly when you do. For
# example, if you have several users for a website, each with
# a unique username, you can use the usernames as the keys
# in a dictionary. You can then store information about each
# user by using a dictionary as the value associated with their
# username. In the following listing, we store three pieces of
# information about each user: their first name, last name,
# and location. We’ll access this information by looping
# through the usernames and the dictionary of information
# associated with each username:

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# We first define a dictionary called users with two keys: one
# each for the usernames 'aeinstein' and 'mcurie'. The value
# associated with each key is a dictionary that includes each
# user’s first name, last name, and location. Then, we loop
# through the users dictionary ❶. Python assigns each key to
# the variable username, and the dictionary associated with
# each username is assigned to the variable user_info. Once
# inside the main dictionary loop, we print the username ❷.
# Then, we start accessing the inner dictionary ❸. The
# variable user_info, which contains the dictionary of user
# information, has three keys: 'first', 'last', and 'location'.
# We use each key to generate a neatly formatted full name
# and location for each person, and then print a summary of
# what we know about each user ❹
