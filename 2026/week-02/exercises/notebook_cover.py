# Write a function called create_notebook() that has a default size of "A4"
# and a default title of "My Notes". The function should print a sentence
# describing the notebook.
# Create a notebook using only the default values.
# Create a notebook with a different size but the default title.
# Create a notebook with both a different size and a different title.

def create_notebook(size="A4", title="My Notes"):
    """Summarize the notebook that is going to be made."""
    print(f"\nI'm going to make a {size} notebook.")
    print(f"It will say, '{title}'.")


create_notebook()
create_notebook(size="A3")
create_notebook(size="B1", title="My Gym Progress")
