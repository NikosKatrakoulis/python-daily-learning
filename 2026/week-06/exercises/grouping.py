# Given a text with dates in the form DD/MM/YYYY.
# Write a program that:
# finds all dates
# uses groups to separate day, month, and year
# prints each date in detail
# Goal: parentheses (), groups

import re

text = input("Enter a date (form DDD/MM/YYYY):")

pattern = re.compile(r"(\d{2})/(\d{2})/(\d{4})")

for match in pattern.finditer(text):
    day, month, year = match.groups()
    print(f"Date -> Day: {day}, Month: {month}, Year: {year}")
