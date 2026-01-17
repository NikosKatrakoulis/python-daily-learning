# Start with your work from Exercise 9-8 (page 173). Store the classes
#  User, Privileges and Admin in one module. Create a separate file,
# make an Admin instance, and call show_priveleges() to show that
# everything is working correctly.

from privileges import Admin

admin = Admin('giorgos', 'papadopoulos', 'geogeop',
              'giogigog@sample.com', 'athens')
admin.privileges.show_privileges()
