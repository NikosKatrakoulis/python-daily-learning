# Write a program that:
# checks if a string is a phone number in the form 123-456-7890
# uses regex to perform the validation
# prints whether the number is valid or not
# Goal: characters, \d, {}

import re

phone_number = input("Give me a phone number (e.g. 123-456-7890):")

pattern = re.compile(r"^\d{3}-\d{3}-\d{4}$")

if pattern.search(phone_number):
    print("The phone number is valid.")
else:
    print("The phone number is invalid.")
