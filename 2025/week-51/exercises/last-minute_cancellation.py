guest_list = ['meleti', 'sofaki', 'thaki']

removed_guest1 = guest_list.pop()
removed_guest2 = guest_list.pop(0)

print(f"{removed_guest1.title()} unfortunately I can not make it for today's dinner. I will call you to rearrange it.")
print(f"{removed_guest2.title()} unfortunately I can not make it for today's dinner. I will call you to rearrange it.")
print(
    f"{guest_list[0].title()} mou, we are gonna go to Village tonight to watch Zoopolis 2.")
del guest_list[0]
print(guest_list)
