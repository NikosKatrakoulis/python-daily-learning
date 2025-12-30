# users = []

# if not users:
#     print("We need to find some users!")
# else:
#     for user in users:
#         if user.lower() == 'admin':
#             print("Hello admin, would you like to see a status report?")
#         else:
#             print(f"Hello {user}, welcome back!")

user_names = ['admin', 'tsaxpinis1222', 'nixterida55',
              'buddyrich', 'papaki@92', 'troler7655']

if not user_names:
    print("We need to find some users!")
else:
    print("The list is not empty.")

user_names = []

if not user_names:
    print("We need to find more users!")

user_names.append('admin')
user_names.append('bbking')
user_names.append('budy')

for user in user_names:
    print(f"Hello, {user}! Welcome back!")
