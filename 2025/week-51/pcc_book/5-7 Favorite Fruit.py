favorite_fruits = ['grape', 'watermelon', 'banana']
fruit = 'apple'

if fruit in favorite_fruits:
    print(f"{fruit.title()} is nice to eat before you go to the gym.")
elif fruit not in favorite_fruits:
    print(f"I'm sorry but I ate all the {fruit} cake.")
elif fruit == 'banana':
    print(f"My mother makes incredible banana cake which my girlfriend loves.")
elif fruit == 'watermelon':
    print("I like to eat only the 'heart' of the watermelon.")
elif fruit == 'grape':
    print("I think that grape is my favorite fruit overall.")
