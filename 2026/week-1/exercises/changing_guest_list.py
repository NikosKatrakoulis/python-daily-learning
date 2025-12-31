# Changing Guest List: You just heard that one of your guests
# can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite. Start with your program
# from Exercise 3-4. Add a print() call at the end of your program, stating
# the name of the guest who can’t make it. Modify your list, replacing the
# name of the guest who can’t make it with the name of the new person you
# are inviting. Print a second set of invitation messages, one for each person
# who is still in your list.


guest_list = ['sofia', 'meletis', 'dimitris']

guest_list.pop()
print(
    f"Hello {guest_list[0].title()}, unfortunately Dimitris can not make it on Sunday.")
print(
    f"Hello {guest_list[1].title()}, unfortunately Dimitris can not make it on Sunday.")

guest_list.append('giorgos')
print(
    f"Hello again {guest_list[0].title()}, I'd like to invite you to dinner on Sunday evening.")
print(
    f"Hello again {guest_list[1].title()}, I'd like to invite you to dinner on Sunday evening.")
print(
    f"Hello again {guest_list[2].title()}, I'd like to invite you to dinner on Sunday evening.")
