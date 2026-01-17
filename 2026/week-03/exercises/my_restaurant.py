# Using your latest Restaurant class, store it in a module.
# Make a separate file that imports Restaurant. Make a Restaurant
# instance, and call one of Restaurant's methods to show that the
# import statement is working properly.

from restaurant import Restaurant

alio = Restaurant('Alio', 'pizza')
alio.describe_restaurant()
alio.open_restaurant()

anemologio = Restaurant('anemologio', 'souvlaki')
anemologio.describe_restaurant()
anemologio.open_restaurant()
