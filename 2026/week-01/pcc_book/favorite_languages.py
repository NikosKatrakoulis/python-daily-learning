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
print(f"Sarah's favorite language is {language}.")

# We use this syntax to pull Sarah’s favorite language from
# the dictionary ❶ and assign it to the variable language.
# Creating a new variable here makes for a much cleaner
# print() call. The output shows Sarah’s favorite language.
