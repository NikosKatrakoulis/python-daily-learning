# Now let’s write a new program that greets a user whose
# name has already been stored:

from pathlib import Path
import json

path = Path(
    "username.json")
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")

# We read the contents of the data file ❶ and then use
# json.loads() to assign the recovered data to the variable
# username ❷. Since we’ve recovered the username, we can
# welcome the user back with a personalized greeting.
