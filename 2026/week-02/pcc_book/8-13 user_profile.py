# User Profile: Start with a copy of user_profile.py from page 148.
# Build a profile of yourself by calling build_profile(), using your first and last
# names and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):

    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info


user_profile = build_profile(
    'nikos', 'katrakoulis', location='Megara', studies='MSc in Software Development', interest='AI Engineering')
print(user_profile)
