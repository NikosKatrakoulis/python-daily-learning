# Write different versions of either Exercise 7-4 or 7-5 that do each of
# the following at least once: Use a conditional test in the while
# statement to stop the loop. Use an active variable to control how
# long the loop runs. Use a break statement to exit the loop when the
# user enters a 'quit' value.


prompt = "What topping would you like on your pizza?"
prompt += "\nEnter 'quit when you are finished:"

while True:
    topping = input(prompt)
    if topping == "quit":
        break

    print(f"I will add {topping} to your pizza.")


prompt = "What topping would you like on your pizza?"
prompt += "\nEnter 'quit when you are finished:"

active = True

while active:
    topping = input(prompt)

    if topping == "quit":
        active = False
    else:
        print(f"I will add {topping} to your pizza.")


prompt = "What topping would you like on your pizza?"
prompt += "\nEnter 'quit when you are finished:"

topping = ""

while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f"I will add {topping} to your pizza.")
