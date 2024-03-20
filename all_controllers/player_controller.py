import sys
sys.path.append(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament")
import json
from all_models.player import Player
from all_views.player_view import PlayerView


class PlayerController:
    def __init__(self):
        self.player_view = PlayerView()

    def create_player(self, name, last_name, date_of_birth, chess_id):
        player = Player(name, last_name, date_of_birth, chess_id)
        return player

        
    def save_player(self, player):
        # player_data = player.serialized_player()
        player_data = {
        "name": player.name,
        "last_name": player.last_name,
        "date_of_birth": player.date_of_birth,
        "chess_id": player.chess_id
        }
        try:
            with open(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament\all_data\players.json", 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        data.append(player_data)
        with open(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament\all_data\players.json", "w") as file:
            json.dump(data, file)   

    def show_player(self, player):
        self.player_view.display_player(player)
        
        
# juste pour test du code        
run_for_test = PlayerController()
test_player = run_for_test.create_player("John", "Doe", "1990-01-01", "12345")
run_for_test.save_player(test_player)
# print("Données à enregistrer :", data)
# test = PlayerController()
# testtest = test.serialized_player( "John", "Doe", "1990-01-01", "12345")
# print(testtest)