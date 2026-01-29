# Ask the user to enter shopping categories in one line, separated by commas
# (for example: "fruits, vegetables, drinks").
# Use split(',') to convert the input into a list
# Remove extra spaces around each category
# Print the categories joined by " / " using join()

shopping_list = input(
    "Enter shopping categories in one line,separated by commas.")

shopping_categories = shopping_list.split(",")

clean_categories = []

for category in shopping_categories:
    clean_categories.append(category.strip())

result = " | ".join(clean_categories)
print(result)
