import sys
import os
# Relative path
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

import json
from all_models.player import Player
from all_views.player_view import PlayerView

from dataclasses import asdict, is_dataclass
from datetime import datetime
from typing import Optional

class PlayerController:
    def __init__(self):
        self.player_view = PlayerView()

    def create_player(self):
        name, last_name, date_of_birth, chess_id = self.player_view.get_player_details()
        player = Player(name, last_name, date_of_birth.strftime("%d/%m/%Y"), chess_id)
        self.save_player(player)  # Pass the Player object directly
        return player

    def save_player(self, player):
        if not is_dataclass(player):
            raise TypeError("save_player expects a dataclass instance")
        
        player_data = asdict(player)  # Convert Player object to dictionary
        try:
            with open(os.path.join(project_dir, "all_data", "players.json"), 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(player_data)

        with open(os.path.join(project_dir, "all_data", "players.json"), "w") as file:
            json.dump(data, file, indent=4)
        print("Joueur enregistré avec succès")

    def display_players(self):
        try:
            with open(os.path.join(project_dir, "all_data", "players.json"), 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        for player in data:
            print(f"Joueur: {player['name']} {player['last_name']}")
            print(f"date de naissance: {player['date_of_birth']}")
            print(f"Identifian National d'Echecs: {player['chess_id']}")
        
# player_controller = PlayerController()
# new_player = player_controller.create_player()
# player_controller.save_player(new_player)

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