# Rather than breaking out of a loop entirely without
# executing the rest of its code, you can use the continue
# statement to return to the beginning of the loop, based on
# the result of a conditional test. For example, consider a loop
# that counts from 1 to 10 but prints only the odd numbers in
# that range:

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Every while loop needs a way to stop running so it won’t
# continue to run forever. For example, this counting loop
# should count from 1 to 5:
# This loop runs foverver!
x = 1
while x <= 5:
    print(x)
