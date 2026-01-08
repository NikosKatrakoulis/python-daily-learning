from pathlib import Path

path = Path(__file__).parent / "pi_digits.txt"
contents = path.read_text()
contents = contents.lstrip()
print(contents)


# from pathlib import Path

# print("CWD:", Path.cwd())
# print("SCRIPT FOLDER:", Path(__file__).parent)

# path = Path("pi_digits.txt")
# print("LOOKING FOR:", (Path(__file__).parent / "pi_digits.txt"))
# print("EXISTS?", (Path(__file__).parent / "pi_digits.txt").exists())

# contents = (Path(__file__).parent /
#             "pi_digits.txt").read_text(encoding="utf-8")
# print(contents)
