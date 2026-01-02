#  Favorite Numbers: Modify your program from Exercise 6-2 (page 98)
# so each person can have more than one favorite number. Then print
# each person’s name along with their favorite numbers.

favorite_numbers = {
    'john': [5, 22, 3, 555, 6789],
    'sarah': [28, 2, 88, 190],
    'eric': [35, 1, 17, 2999],
    'nick': [27, 22],
    'alex': [88, 8, 18],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")
