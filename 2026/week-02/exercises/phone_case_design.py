# Write a function called design_case() that has a default color of "black"
# and a default text of "Keep it simple". The function should print a
# summary of the phone case design.
# Make a phone case using all default values.
# Make a phone case with a different color and the default text.
# Make a phone case with a different color and a different text.

def design_case(color='black', text='Keep it simple'):
    """Summarize the phone case that is going to be made."""
    print(f"\nI'm going to make a {color} phone case.")
    print(f"it will say, '{text}'.")


design_case()
design_case(color="red")
design_case(color="green", text="I love Sofaki")
