requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")


requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese")

print("\nFinished making your pizza!\n")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")

print("\nFinished making your pizza.\n")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry we are out of green peppers right now.")
    else:
        print(F"Adding {requested_topping}")

print("\nFinished making your pizza!\n")


requested_toppings = []

if requested_toppings:
    for request_topping in requested_toppings:
        print(f"Adding {request_topping}.")
    print("\nFinishing making your pizza.")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives',
                      'green peppers', 'pepperoni', 'pinapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinishing making your pizza.")
