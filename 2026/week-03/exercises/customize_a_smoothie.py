# Write a function called make_smoothie() that accepts any number of
# ingredients. The function should print a summary of the smoothie that
# is being prepared. Call the function three times, using a different
# number of ingredients each time.

def make_smoothie(*ingredients):
    """Make a smoothie with the given ingredients."""
    print("\nI'll make you a great smoothie.")
    for ingredient in ingredients:
        print(f" ...adding {ingredient} to your smoothie.")
    print("Your smoothie is ready!")


make_smoothie('almond milk', 'oats', 'black chocolate', 'honey')
make_smoothie('milk', 'yogurt', 'blueberries', 'protein scoope')
make_smoothie('banana', 'apple', 'strawberry', 'milk', 'stevia')
