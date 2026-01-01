# You can also use a dictionary to store one kind of information about
# many objects. For example, say you want to poll a number
# of people and ask them what their favorite programming
# language is. A dictionary is useful for storing the results of a
# simple poll, like this:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

# To use this dictionary, given the name of a person who
# took the poll, you can easily look up their favorite language:

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.\n")

# We use this syntax to pull Sarah’s favorite language from
# the dictionary ❶ and assign it to the variable language.
# Creating a new variable here makes for a much cleaner
# print() call. The output shows Sarah’s favorite language.


for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")


# The keys() method is useful when you don’t need to work
# with all of the values in a dictionary. Let’s loop through the
# favorite_languages dictionary and print the names of
# everyone who took the poll:

for name in favorite_languages.keys():
    print(name.title())

# This for loop tells Python to pull all the keys from the
# dictionary favorite_languages and assign them one at a time
# to the variable name. The output shows the names of
# everyone who took the poll.

# Looping through the keys is actually the default behavior
# when looping through a dictionary, so this code would have
# exactly the same output if you wrote:

for name in favorite_languages:
    print(name.title())

# You can access the value associated with any key you care
# about inside the loop, by using the current key. Let’s print a
# message to a couple of friends about the languages they
# chose. We’ll loop through the names in the dictionary as we
# did previously, but when the name matches one of our
# friends, we’ll display a message about their favorite
# language:


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        print(f"\t{name.title()}, I see you love {language.title()}!")

# You can also use the keys() method to find out if a
# particular person was polled. This time, let’s find out if Erin
# took the poll:

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!\n")

# The keys() method isn’t just for looping: it actually returns
# a sequence of all the keys, and the if statement simply
# checks if 'erin' is in this sequence. Because she’s not, a
# message is printed inviting her to take the poll.

# Looping through a dictionary returns the items in the same
# order they were inserted. Sometimes, though, you’ll want to
# loop through a dictionary in a different order.
# One way to do this is to sort the keys as they’re returned
# in the for loop. You can use the sorted() function to get a
# copy of the keys in order:

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# This for statement is like other for statements, except that
# we’ve wrapped the sorted() function around the
# dictionary.keys() method. This tells Python to get all the
# keys in the dictionary and sort them before starting the
# loop. The output shows everyone who took the poll, with the
# names displayed in order.


# If you are primarily interested in the values that a dictionary
# contains, you can use the values() method to return a
# sequence of values without any keys. For example, say we
# simply want a list of all languages chosen in our
# programming language poll, without the name of the person
# who chose each language:

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# The for statement here pulls each value from the
# dictionary and assigns it to the variable language. When
# these values are printed, we get a list of all chosen
# languages.

# This approach pulls all the values from the dictionary
# without checking for repeats. This might work fine with a
# small number of values, but in a poll with a large number of
# respondents, it would result in a very repetitive list. To see
# each language chosen without repetition, we can use a set.
# A set is a collection in which each item must be unique:

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# You can build a set directly using braces and
# separating the elements with commas:
# >>> languages = {'python', 'rust', 'python', 'c'}
# >>> languages
# {'rust', 'python', 'c'}
# It’s easy to mistake sets for dictionaries because
# they’re both wrapped in braces. When you see braces
# but no key-value pairs, you’re probably looking at a
# set. Unlike lists and dictionaries, sets do not retain
# items in any specific order
