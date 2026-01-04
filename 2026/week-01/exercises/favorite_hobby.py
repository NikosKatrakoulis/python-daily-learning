# Poll users about their favorite hobby and display the results at the end.

responses = {}
active = True


while active:
    name = input("What is your name?")
    hobby = input("What is your favorite hobby?")

    responses[name] = hobby

    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        active = False

print("---Poll Results---")
for name, hobby in responses.items():
    print(f"{name}'s favorite hobby is {hobby}.")
