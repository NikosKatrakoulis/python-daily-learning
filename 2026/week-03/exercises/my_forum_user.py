# Create a module called forum_user.py. Inside this module, store
# the following classes: ForumUser, Moderator (inherits from ForumUser),
# Permissions (stores a list of permissions). The Moderator class should
# have a Permissions object as an attribute.
# Create a separate file called my_forum_user.py.
# Import the Moderator class, create an instance, assign several permissions,
# and call the method that displays them to verify that the import works.

from forum_user import Moderator

nikos = Moderator('papageo', 'gigigi@sample.com', 'zurich')
nikos.describe_user()

nikos_permissions = [
    "can add post",
    "can delete post",
    "can add user",
    "can delete user",
]

nikos.permissions.permissions = nikos_permissions
nikos.permissions.show_permissions()
