# When you use the input() function, Python interprets
# everything the user enters as a string.
# When you try to use the input to do a numerical
# comparison , Python produces an error because it can’t
# compare a string to an integer.
# How do you use the int() function in an actual program?
# Consider a program that determines whether people are tall
# enough to ride a roller coaster:

height = input("How tall are you? in inches?")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# The program can compare height to 48 because height =
# int(height) converts the input value to a numerical
# representation before the comparison is made.
# When you use numerical input to do calculations and
# comparisons, be sure to convert the input value to a
# numerical representation first.
