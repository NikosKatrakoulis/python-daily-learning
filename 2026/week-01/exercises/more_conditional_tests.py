# More Conditional Tests: You don’t have to limit the
# number of tests you create to 10. If you want to try more
# comparisons, write more tests and add them to conditional_tests.py.
# Have at least one True and one False result for each of the following:
# Tests for equality and inequality with strings Tests using the lower()
# method Numerical tests involving equality and inequality, greater than
# and less than, greater than or equal to, and less than or equal to
# Tests using the and keyword and the or keyword Test whether an item
# is in a list Test whether an item is not in a list.

# Strings

car = "Subaru"

print("\nIs car =='Subaru'? I predict True.")
print(car == "Subaru")

print("\nIs car != 'Subaru'? I predict False.")
print(car != "Subaru")

# Lower() method

print("\nIs car.lower() = 'subaru'? I predict True.")
print(car.lower() == 'subaru')

print("\nIs car.lower() == 'suBAru? I predict False.")
print(car.lower() == 'suBARu')

# Numerical Tests

number = 10

print("\nIs number == 10? I predict True.")
print(number == 10)

print("\nIs number != 10? I predict False.")
print(number != 10)

print("\nIs number > 5? I predict True.")
print(number > 5)

print("\nIs number < 5? I predict False.")
print(number < 5)

print("\nIs number >= 10? I predict True.")
print(number >= 10)

print("\nIs number <= 5? I predict False.")
print(number <= 5)

# and / or keywords

age = 25

print("\nIs age > 18 and age < 40? I predict True.")
print(age > 18 and age < 40)

print("\nIs age > 30 and age < 40? I predict False.")
print(age > 30 and age < 40)

print("\nIs age < 18 or age > 20? I predict True.")
print(age < 18 or age > 20)

print("\nIs age < 18 or age> 30? I predict False.")
print(age < 18 or age > 30)
