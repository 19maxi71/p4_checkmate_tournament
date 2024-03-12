class PlayerView:
    def display_player(self, player):
        print(f"Player: {player.name} {player.last_name}")
        print(f"Date of Birth: {player.date_of_birth}")
        print(f"Chess ID: {player.chess_id}")