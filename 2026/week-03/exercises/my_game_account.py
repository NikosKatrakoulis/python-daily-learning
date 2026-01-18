# Create a module called game_account.py. Inside this module,
# store the following classes: Player, GameAdmin (inherits from Player),
# AdminPowers (stores a list of admin powers). The GameAdmin class
# should include an AdminPowers instance. Create a separate file
# called my_game_account.py. Import the GameAdmin class, create an
# instance, assign several admin powers, and call the method that
# displays them to confirm everything is working correctly.

from game_account import GameAdmin

admin = GameAdmin('papasouzas', 99)
admin.describe_player()

admin_powers = [
    "add/delete life to players",
    "add/delete strength to players",
    "add/delete skills to players"
]

admin.powers.powers = admin_powers
admin.powers.show_powers()
