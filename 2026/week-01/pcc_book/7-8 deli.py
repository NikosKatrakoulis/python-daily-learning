# Deli: Make a list called sandwich_orders and fill it with the names
# of various sandwiches. Then make an empty list called finished_
# sandwiches. Loop through the list of sandwich orders and print a
# message for each order, such as I made your tuna sandwich. As each
# sandwich is made, move it to the list of finished sandwiches. After
# all the sandwiches have been made, print a message listing each
# sandwich that was made in finished_sandwiches.

sandwich_orders = ['pulled pork v2', 'pancetta v1', 'pulled pork v3',
                   'pulled pork v3', 'crispy chicken', 'pulled pork v3']

finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"\n I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)


print("\n- - -Finished Sandwiches- - -")
for sandwich in finished_sandwiches:
    print(sandwich.title())
