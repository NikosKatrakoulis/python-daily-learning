# Create a multiline string with 3–5 lines.
# Use split('\n') to get a list of lines. Print each line with a number
# prefix (1), (2), (3), etc.
# (Optional) Rebuild the multiline string using "\n".join(...).

text = """Dear Sofaki mou,
I want to tell you that I will be a little bit delayed because I stucked in a traffic jam.
I will be there around 22:00!"""

lines = text.split('\n')

for i, line in enumerate(lines, start=1):
    print(f"({i}) {line}")

rebuilt_text = "\n".join(lines)
print("\nRebuilt text:\n")
print(rebuilt_text)
