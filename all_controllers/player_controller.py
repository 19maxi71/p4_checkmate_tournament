from player.py import Player
from player_view.py import PlayerView


class PlayerController:
    def __init__(self):
        self.player_view = PlayerView()

    def create_player(self, name, last_name, date_of_birth, chess_id):
        player = Player(name, last_name, date_of_birth, chess_id)
        
    def show_player(self, player):
        self.player_view.display_player(player)