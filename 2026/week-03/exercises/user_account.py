# Write a function called create_user() that always receives a username and
# an email. The function should accept any number of keyword arguments
# describing extra user details (for example: age, country, premium_user).
# Call the function with the required information and at least two additional
# keyword arguments. Print the dictionary that’s returned.

def create_user(username, email, **details):
    """Make a dictionary representing an account."""
    user_dict = {
        'Username': username,
        'Email': email,
    }
    for detail, value in details.items():
        user_dict[detail] = value
    return user_dict


new_user = create_user(
    'nikokat223', 'nikokkkattt@example.com', age=18, country="Greece")
print(new_user)
current_user = create_user(
    'gioviniino12345', 'giogiogiovanni@pvvcc.com', premium_user=True)
print(current_user)
old_user = create_user(
    'giota99', 'giotakamperidou@exampleexample.com.gr', age=55)
print(old_user)
