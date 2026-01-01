"""
game.py
This file contains the game engine: input parsing, commands and the main loop.
"""

from typing import Dict, List, Tuple, Optional


def print_help() -> None:
    print("\nCommands:")
    print("   look")
    print("   go <north|south|east|west|up|down")
    print("   take <item>")
    print("   inventory")
    print("   help")
    print("   quit")


def normalize_direction(dir_word: str) -> str:
    """Allow short directions like 'n' -> 'north'."""
    mapping = {
        "n": "north",
        "s": "south",
        "e": "east",
        "w": "west",
        "u": "up",
        "d": "down",
    }
    return mapping.get(dir_word, dir_word)


def parse_command(raw: str) -> Tuple[str, List[str]]:
    """
    Turn a raw user input string into:
    verb: first word (e.g 'go')
    args: the remaining words (e.g['north'])
    """

    cleaned = raw.strip().lower()
    if not cleaned:
        return "", []
    parts = cleaned.split()
    return parts[0], parts[1:]


class Game:
    def __init__(
        self,
        rooms: Dict[str, Dict],
        start_room: str,
        win_room: str,
        locked_room: Optional[str] = None,
        required_item_for_lock: Optional[str] = None,
    ) -> None:
        self.rooms = rooms
        self.current_room = start_room
        self.win_room = win_room
        self.locked_room = locked_room
        self.required_item_for_lock = required_item_for_lock
        self.inventory: List[str] = []

    def describe_current_room(self) -> None:
        room = self.rooms[self.current_room]
        print("\n" + room["desc"])

        exits = ", ".join(room["exits"].keys())
        print(f"Exits: {exits}")

        items = room.get("items", [])
        if items:
            print("You see:", ", ".join(items))
        else:
            print("You see nothing.")

    def show_inventory(self) -> None:
        if self.inventory:
            print("Inventory:", ", ".join(self.inventory))
        else:
            print("Your inventory is empty.")

    def take(self, item_name: str) -> None:
        items_here = self.rooms[self.current_room].get("items", [])
        if item_name in items_here:
            items_here.remove(item_name)
            self.inventory.append(item_name)
            print(f"You took the {item_name}.")
        else:
            print("That item is not here.")

    def can_enter(self, next_room: str) -> bool:
        """
        If a room is locked, you can only enter it if you have the required item.
        """

        if self.locked_room and next_room == self.locked_room:
            if self.required_item_for_lock and self.required_item_for_lock not in self.inventory:
                print("The door is locked. You need a key.")
                return False
        return True

    def move(self, direction: str) -> None:
        direction = normalize_direction(direction)

        exits = self.rooms[self.current_room]["exits"]
        if direction not in exits:
            print("You can't go that way.")
            return

        next_room = exits[direction]
        if not self.can_enter(next_room):
            return

        self.current_room = next_room
        self.describe_current_room()

    def is_won(self) -> None:
        return self.current_room == self.win_room

    def run(self) -> None:
        print("Welcome to the Text Adventure!")
        print_help()
        self.describe_current_room()

        while True:
            raw = input("\n>")
            verb, args = parse_command(raw)

            if verb == "":
                continue

            if verb == "help":
                print_help()

            elif verb == "look":
                self.describe_current_room()

            elif verb == "inventory":
                self.show_inventory()

            elif verb == "take":
                if not args:
                    print("Usage: take<item>")
                    continue
                self.take(args[0])

            elif verb == "go":
                if not args:
                    print("Usage: go <direction>")
                    continue
                self.move(args[0])

                if self.is_won():
                    print("\nYOU WIN! Thanks for playing.")
                    break

            elif verb == "quit":
                print("Goodbye!")
                break

            else:
                print("I don't understand.Type 'help to see commands.")
