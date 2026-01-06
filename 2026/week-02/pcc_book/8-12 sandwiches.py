# Sandwiches: Write a function that accepts a list of items a person
# wants on a sandwich. The function should have one parameter that collects
# as many items as the function call provides, and it should print a summary
# of the sandwich that’s being ordered. Call the function three times, using a
# different number of arguments each time.

def make_sandwich(*items):
    print("\nThe next sandwich has the items:")
    for item in items:
        print(f"- {item}")
    print("Your sandwich is ready!")


make_sandwich('cheese', 'chicken', 'tomato')
make_sandwich('cheese', 'fries', 'mayo', 'ketchap')
make_sandwich('crispy chicken', 'fries', 'lettuce', 'onions', 'garlic sauce')
