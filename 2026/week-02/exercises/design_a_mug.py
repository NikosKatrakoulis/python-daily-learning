# Write a function called design_mug() that accepts a color and a message.
# The function should print a sentence summarizing the mug color and the
# message printed on it. Call the function once using positional arguments
#  and once using keyword arguments.

def design_mug(color, message):
    """Summarize the mug thay is going to be made."""
    print(f"\nI'm going to made a {color} mug.")
    print(f"It'll say, '{message}'.")


design_mug('red', 'Merry Christmas')
design_mug('blue', 'Happy Easter')
