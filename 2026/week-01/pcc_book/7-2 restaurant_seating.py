# Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a
# message saying they’ll have to wait for a table. Otherwise, report
# that their table is ready.

dinner_group = input("How many people are in the dinner group?")
dinner_group = int(dinner_group)

if dinner_group > 8:
    print("You'll have to wait for a table.")
else:
    print("The table is ready!")
