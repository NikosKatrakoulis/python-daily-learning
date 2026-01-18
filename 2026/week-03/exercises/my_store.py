# Create a class called Store and save it in a file called store.py.
# The class should include attributes like store name and store type,
# and a method that prints a short description of the store.
# Create a second file called my_store.py.
# Import the Store class, create an instance of it, and call one
# of its methods to show that the import is working as expected.

from store import Store

helpviaai = Store('helpvia.ai', 'ai')
helpviaai.describe_store()
