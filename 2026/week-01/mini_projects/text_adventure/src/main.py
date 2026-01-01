"""
main.py
Entry point for the game.
"""

from world import ROOMS, START_ROOM, WIN_ROOM, LOCKED_ROOM, REQUIRED_ITEM_FOR_LOCK
from game import Game


def main() -> None:
    game = Game(
        rooms=ROOMS,
        start_room=START_ROOM,
        win_room=WIN_ROOM,
        locked_room=LOCKED_ROOM,
        required_item_for_lock=REQUIRED_ITEM_FOR_LOCK,
    )
    game.run()


if __name__ == "__main__":
    main()
