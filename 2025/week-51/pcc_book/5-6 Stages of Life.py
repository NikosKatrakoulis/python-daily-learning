age = 65

if age < 2:
    output = "baby"
elif age >= 2 and age < 4:
    output = "toddler"
elif age >= 4 and age < 13:
    output = "kid"
elif age >= 13 and age < 20:
    output = "teenager"
elif age >= 20 and age < 65:
    output = "adult"
elif age >= 65:
    output = "elder"

print(f"The person is {output}.")
