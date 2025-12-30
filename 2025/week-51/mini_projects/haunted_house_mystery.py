import sys


def print_intro():
    print("========================================")
    print("          HAUNTED HOUSE MYSTERY         ")
    print("========================================")
    player_name = input("What is your name, wanderer?")
    print(f"\nWelcome, {player_name}.")
    print("You stand at the entrance of an old, abandoned mansion.")
    print("A chilling presence surrounds you. A restless spirit haunts this place.")
    print("Your goal: find the sacred amulet and escape the haunted house alive.\n")
    return player_name


def print_status(lives, inventory):
    print("\n----------------------------------------")
    print(f"Lives: {lives}")
    if isinstance(inventory, list):
        if inventory:
            print("Inventory:", ",".join(inventory))
        else:
            print("Inventory: (empty).")
    else:
        print("ERROR: Inventory is not a list", inventory)
    print("\n----------------------------------------")


def get_player_choice():
    print("\nYou can move right / left / forward / quit")
    choice = input("What do you want to do?").strip().lower()
    return choice


def handle_left_room(inventory):
    if 'amulet' in inventory:
        print("There is nothing new here.")
    else:
        print("You are in a big library and you need to find a way to leave from there.")
    inventory.append('amulet')
    return inventory
