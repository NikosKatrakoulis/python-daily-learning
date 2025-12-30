guest_list = ['Sofaki', 'Dimitri', 'Meleti']
absent_guest = guest_list.pop(1)
print(f"Hello, {absent_guest}. I'm so sorry to hear that you will not be able to attend to my dinner.")

guest_list.append('Gino')
for i in guest_list:
    print(f"Hello {i}, I want to invite you to dinner on Sunday evening.")
