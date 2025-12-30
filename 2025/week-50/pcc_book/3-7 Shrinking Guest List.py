guest_list = ['Thaki', 'Sofaki', 'Giorgo', 'Meleti', 'Dimitri', 'Gino', 'Niko']
for i in guest_list:
    print(f"\nHey {i}, I just got informed that the lunch table won't arrive in time and I can invite only two people for dinner.")

not_guest = guest_list.pop()
print(f"\n{not_guest} I'm so sorry that I can't invite you to lunch. Maybe next weekend I will rearrange it.")
not_guest = guest_list.pop()
print(f"\n{not_guest} I'm so sorry that I can't invite you to lunch. Maybe next weekend I will rearrange it.")
not_guest = guest_list.pop()
print(f"\n{not_guest} I'm so sorry that I can't invite you to lunch. Maybe next weekend I will rearrange it.")
not_guest = guest_list.pop()
print(f"\n{not_guest} I'm so sorry that I can't invite you to lunch. Maybe next weekend I will rearrange it.")
not_guest = guest_list.pop()
print(f"\n{not_guest} I'm so sorry that I can't invite you to lunch. Maybe next weekend I will rearrange it.")


print(f"{guest_list[0]} you are still invited to lunch.")
print(f"{guest_list[1]} you are still invited to lunch.")

del guest_list[0]
del guest_list[0]
print(guest_list)
