# Exercise:
# Write three versions of a program that asks users for song requests
# until they enter quit.
# Use:

# a conditional test in while

# an active variable

# a break statement

# Version #1
# song = ""

# while song != 'quit':
#     song = input("Enter a song(type 'quit' to stop):")
#     if song != 'quit':
#         print(f"Adding {song} to the playlist.")

# Version #2
# active = True

# while active:
#     song = input("Enter a song(type 'quit' to stop):")

#     if song == 'quit':
#         active = False
#         print(f"Adding {song} to the playlist.")

# Version #3
while True:
    song = input("Enter a song(type 'quit' to stop):")

    if song == 'quit':
        break

    print(f"Adding {song} to the playlist.")
