guest_list = ['Sofaki', 'Meleti', 'Dimitri', 'Gino']
for i in guest_list:
    print(
        f"\nHello {i}, I found a bigger table for the barbeque afternoob so I will call 3 more people.")

guest_list.insert(0, 'Thaki')
guest_list.insert(2, 'Giorgo')
guest_list.append('Niko')
for i in guest_list:
    print(f"\nHey {i}, I finally found a big table so you are invited for a lunch on my place on Sunday. Bring your positive energy.")
