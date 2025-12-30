guest_list = ['meleti', 'sofaki', 'thaki']

print(
    f"{guest_list[0].title()}, I found a bigger table and I will invite three more people for the BBQ.")
print(
    f"{guest_list[1].title()}, I found a bigger table and I will invite three more people for the BBQ.")
print(
    f"{guest_list[2].title()}, I found a bigger table and I will invite three more people for the BBQ.")

guest_list.insert(0, 'dimitri')
guest_list.insert(2, 'giorgo')
guest_list.append('philippe')

print(
    f"Hey {guest_list[0].title()}, I want to invite you for a BBQ on Saturday at 15:00")
print(
    f"Hey {guest_list[1].title()}, I want to invite you for a BBQ on Saturday at 15:00")
print(
    f"Hey {guest_list[2].title()}, I want to invite you for a BBQ on Saturday at 15:00")
print(
    f"Hey {guest_list[3].title()}, I want to invite you for a BBQ on Saturday at 15:00")
print(
    f"Hey {guest_list[4].title()}, I want to invite you for a BBQ on Saturday at 15:00")
print(
    f"Hey {guest_list[5].title()}, I want to invite you for a BBQ on Saturday at 15:00")
