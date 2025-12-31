rooms = {
    "hall": {
        "description": "You are in the main hall. Old pictures hang on the walls",
        "exits": {"north": "kitchen", "east": "study"},
        "items": []
    },
    "kitchen": {
        "description": "You are in the kitchen. It smells like burnt bread. Something shiny is near the sink.",
        "exits": {"south": "hall"},
        "items": ["key"]
    },
    "study": {
        "description": "You are in a dusty study. Books cover the shelves. A small note is on the desk.",
        "exits": {"west": "hall", "east": "gate"},
        "items": ["note"]
    },
    "basement": {
        "description": "You are in the basement. The air is cold and damp. You hear dripping water.",
        "exits": {"up": "hall"},
        "items": []
    },
    "gate": {
        "description": "You are in front of a heave exit door. It look locked.",
        "exits": {"west": "study"},
        "items": []
    }
}
