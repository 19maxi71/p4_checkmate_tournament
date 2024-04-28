import sys
sys.path.append(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament")
import json
from all_models.player import Player
from all_views.player_view import PlayerView


from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional

class PlayerController:
    def __init__(self):
        self.player_view = PlayerView()

    def create_player(self):
        name, last_name, date_of_birth, chess_id = self.player_view.get_player_details()
        player = Player(name, last_name, date_of_birth.strftime("%d/%m/%Y"), chess_id)
        return asdict(player)

    def save_player(self, player):
        player_data = player
        try:
            with open(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament\all_data\players.json", 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(player_data)

        with open(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament\all_data\players.json", "w") as file:
            json.dump(data, file)
        

    def display_players(self):
        try:
            with open(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament\all_data\players.json", 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        for player in data:
            print(f"Joueur: {player['name']} {player['last_name']}")
            print(f"date de naissance: {player['date_of_birth']}")
            print(f"Identifian National d'Echecs: {player['chess_id']}")
        
player_controller = PlayerController()
new_player = player_controller.create_player()
player_controller.save_player(new_player)

# test = PlayerController()
# testtest = test.display_players()
        
# # juste pour test du code        
# run_for_test = PlayerController()
# test_player = run_for_test.create_player()
# run_for_test.save_player(test_player)


# print("Données à enregistrer :", data)
# test = PlayerController()
# testtest = test.serialized_player( "John", "Doe", "1990-01-01", "12345")
# print(testtest)