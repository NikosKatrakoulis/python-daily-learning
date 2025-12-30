age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# Rather than printing the admission price within the if-elif
# else block, it would be more concise to set just the price
# inside the if-elif-else chain and then have a single print()
# call that runs after the chain has been evaluated
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")
