# Given an email like "nikos.k@example.com", use split('@') to
# separate the username and domain.
# Then split the domain using split('.') to get the site name and the
# top-level domain. Print all parts.

email = input("Enter your email address:")

username, domain = email.split('@')

site_name, top_level_domain = domain.split('.')

print("Username:", username)
print("Site name:", site_name)
print("Top-level domain:", top_level_domain)
