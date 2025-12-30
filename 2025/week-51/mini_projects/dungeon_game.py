import sys


def print_intro():
    print("========================================")
    print("        WELCOME TO THE DUNGEON          ")
    print("========================================")
    player_name = input("What is your name, adventurer?")
    print(f"\nNice to meet you,{player_name}!")
    print("You wake up in a dark and cold dungeon.")
    print("The goal is simple:ESCAPE before you lose all your lives.\n")
    return player_name


def print_status(lives, inventory):
    print("\n-----------------------------------------")
    print(f"Lives: {lives}")
    if isinstance(inventory, list):
        if inventory:
            print("Inventory: ", ", ".join(inventory))
        else:
            print("Inventory: (empty)")
    else:
        print("ERROR: inventory is not a list!", inventory)
    print("-----------------------------------------")


def get_player_choice():
    print("\nYou can choose: left / right / forward / quit")
    choice = input("What do you want to do?").strip().lower()
    return choice


def handle_left_room(inventory):
    if "key" in inventory:
        print("You return to the room where you found the key. There is nothing new here.")
    else:
        print("You enter a small room lit by candles.")
        print("A friendly elf appears and hands you a shiny key")
        print("You carefully put the key in your pocket.")
        inventory.append('key')
    return inventory


def handle_right_room(lives):
    print("You walk to the right...")
    print("Suddenly, the floor collapses beneath you!")
    print("You manage to climb back up but you are badly hurt.")
    lives -= 1
    print("You lost one life")
    return lives


def handle_forward_room(lives, inventory):
    escaped = False
    print("You walk forward into a long corridor.")
    print("At the end, you see a massive door with an iron lock.")
    if "key" in inventory:
        print("You take out the key from your pocket.")
        print("The key fits perfectly in the lock...")
        print("The door opens and sunlight hits your face!")
        print("You have escaped the dungeon!")
        escaped = True
    else:
        print("The door is locked. You need a key to open it.")
        print("You feel frustrated and a bit tired.")
        lives -= 1
        print("You lose one life from exhaustion.")
    return lives, escaped


def play_game():
    player_name = print_intro()

    lives = 3
    inventory = []
    escaped = False

    print(f"{player_name}, your adventure begins now...")

    while lives > 0 and not escaped:
        print_status(lives, inventory)
        choice = get_player_choice()

        if choice == 'left':
            inventory = handle_left_room(inventory)
        elif choice == 'right':
            lives = handle_right_room(lives)
        elif choice == 'forward':
            lives, escaped = handle_forward_room(lives, inventory)
        elif choice == 'quit':
            print("\nYou decide to give up and sit on the cold dungeon floor.")
            print("The dungeon keeps you forever...")
            lives = 0
        else:
            print("You hesitate and do nothing. Time passes...")
            print("Your fear drains your energy.You lose one life.")
            lives -= 1

    print("\n=========================================")
    if escaped:
        print("CONGRATULATIONS! YOU ESCAPED!")
    else:
        print("GAME OVER. The dungeon has claimed another soul...")
    print("===========================================")


def main():
    while True:
        play_game()
        answer = input("Do you want to play again? (yes/no)").strip().lower()
        if answer not in ("yes", "y"):
            print("Thank you for playing Goodbye.")
            sys.exit()


if __name__ == "__main__":
    main()
