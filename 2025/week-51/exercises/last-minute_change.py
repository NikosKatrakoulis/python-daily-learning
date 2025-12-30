guest_list = ['meleti', 'sofaki', 'thaki']

guest1 = guest_list.pop()
guest2 = guest_list.pop()
print(f"{guest1.title()}, I'm sorry to hear that you can't make it.")
print(f"{guest2.title()}, I'm sorry to hear that you can't make it.")

guest_list.append('dimitri')
guest_list.append('giorgo')

print(
    f"\n{guest_list[0].title()}, I want to invite you to go in Tropicana on Saturday night.")
print(
    f"{guest_list[1].title()}, I want to invite you to go in Tropicana on Saturday night.")
print(
    f"{guest_list[2].title()}, I want to invite you to go in Tropicana on Saturday night.")

print(guest_list)
