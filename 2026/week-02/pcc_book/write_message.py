from pathlib import Path

path = Path(
    "C://Dev//python-daily-learning//2026//week-02//pcc_book//programming.txt")
path.write_text("I love programming.")
print(path)

# To write more than one line to a file, you need to build a
# string containing the entire contents of the file, and then
# call write_text() with that string. Let’s write several lines to
# the programming.txt file:

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path(
    "C://Dev//python-daily-learning//2026//week-02//pcc_book//programming.txt")
path.write_text(contents)


# Be careful when calling write_text() on a path object.
# If the file already exists, write_text() will erase the
# current contents of the file and write new contents to
# the file. Later in this chapter, you’ll learn to check
# whether a file exists using pathlib.
