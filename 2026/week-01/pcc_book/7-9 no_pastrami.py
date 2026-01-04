# No Pastrami: Using the list sandwich_orders from Exercise 7-8,
# make sure the sandwich 'pastrami' appears in the list at least three times.
# Add code near the beginning of your program to print a message saying
# the deli has run out of pastrami, and then use a while loop to remove
# all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami
# sandwiches end up.

sandwich_orders = ['pulled pork v2', 'pastrami', 'pancetta v1', 'pulled pork v3',
                   'pulled pork v3', 'pastrami',  'crispy chicken', 'pastrami',  'pulled pork v3']

finished_orders = []

print("The deli has run out of pastrami! Sorry for the inconvenience!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_orders.append(current_sandwich)

print(f"\nSandwiches that were made:")
for sandwich in finished_orders:
    print(f" -{sandwich}")
