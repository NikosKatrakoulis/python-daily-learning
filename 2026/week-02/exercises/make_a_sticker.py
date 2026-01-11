# Write a function called create_sticker() that accepts a shape and a text.
# The function should print a sentence describing the sticker shape and the
# text on it. Call the function once using positional arguments and
# once using keyword arguments.

def create_sticker(shape, text):
    """Summarize the sticker that is going to be made."""
    print(f"\nI'm going to make a {shape} sticker.")
    print(f"It will say,'{text}'.")


create_sticker('square', 'hackathon')
create_sticker('triangle', 'anemologio')
