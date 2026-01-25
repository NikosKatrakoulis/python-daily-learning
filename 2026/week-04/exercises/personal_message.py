name = 'nikos'
msg = f"Hello {name.title()}, would you like to learn some Python today?"
print(msg)

msg = 'Hello %s, would you like to learn some Python today?' % (name.title())
print(msg)


msg = 'Hello {}, would you like to learn some Python today?'.format(
    name.title())
print(msg)
