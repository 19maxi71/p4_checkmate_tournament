import os
import sys

# Relative path
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

import json
from all_models.player import Player
from all_views.player_view import PlayerView
from dataclasses import asdict, is_dataclass

class PlayerController:
    def __init__(self):
        self.player_view = PlayerView()

    def create_player(self):
        """Crée un nouveau joueur et l'enregistre."""
        name, last_name, date_of_birth, chess_id = self.player_view.get_player_details()
        player = Player(name, last_name, date_of_birth.strftime("%d/%m/%Y"), chess_id)
        self.save_player(player)  # Pass the Player object directly
        return player

    def save_player(self, player):
        """Enregistre un joueur dans le fichier JSON."""
        if not is_dataclass(player):
            raise TypeError("save_player expects a dataclass instance")
        
        player_data = asdict(player)  # Convert Player object to dictionary
        try:
            with open(os.path.join(os.path.dirname(__file__), '..', 'all_data', 'players.json'), 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(player_data)

        with open(os.path.join(os.path.dirname(__file__), '..', 'all_data', 'players.json'), "w") as file:
            json.dump(data, file, indent=4)
        print("Joueur enregistré avec succès")

    def display_players(self):
        """Affiche tous les joueurs enregistrés."""
        try:
            with open(os.path.join(os.path.dirname(__file__), '..', 'all_data', 'players.json'), 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        for player in data:
            print(f"Joueur: {player['name']} {player['last_name']}")
            print(f"date de naissance: {player['date_of_birth']}")
            print(f"Identifiant National d'Echecs: {player['chess_id']}")