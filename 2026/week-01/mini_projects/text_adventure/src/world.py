"""
world.py
This file contains the game's world data(rooms, descriptions, exits, items).
"""

ROOMS = {
    "hall": {
        "desc": "You are in the main hall. Old pictures hang on the walls. The floor creaks under your feet.",
        "exits": {"north": "kitchen", "east": "study", "down": "basement"},
        "items": []
    },
    "kitchen": {
        "desc": "You are in the kitchen. It smells like burnt bread. Something shiny is near the sink.",
        "exits": {"south": "hall"},
        "items": ["key"]
    },
    "study": {
        "desc": "You are in a dusty study. books cover the shelves. A small note rests on the desk",
        "exits": {"west": "hall", "east": "gate"},
        "items": ["note"]
    },
    "basement": {
        "desc": "You are in the basement. The air is cold and damp. You hear dripping water in the dark.",
        "exits": {"up": "hall"},
        "items": ["coin"]
    },
    "gate": {
        "desc": "You step through the exit door and fell fresh air on your face.",
        "exits": {"west": "study"},
        "items": []
    },
}

START_ROOM = "hall"
WIN_ROOM = "gate"
LOCKED_ROOM = "gate"
REQUIRED_ITEM_FOR_LOCK = "key"
