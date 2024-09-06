import sys
import os
import json
from dataclasses import dataclass, asdict, field
from datetime import datetime
from typing import Optional, List

# Relative path
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

@dataclass
class Player:
    name: str
    last_name: str
    date_of_birth: str
    chess_id: str
    points: Optional[float] = 0.0
    previous_opponents: List[str] = field(default_factory=list)

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            last_name=data['last_name'],
            date_of_birth=data['date_of_birth'],
            chess_id=data['chess_id'],
            points=data.get('points', 0.0),
            previous_opponents=data.get('previous_opponents', [])
        )

    @staticmethod
    def player_exists(player_data):
        try:
            players_data_file_path = os.path.join(project_dir, "all_data", "players.json")
            with open(players_data_file_path, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("ouvre pas ton json machine")  # voir si l'erreur est là
            return False

        for player in data:
            if player['chess_id'] == player_data['chess_id']:
                print(f"Joueur trouvé: {player['name']} {player['last_name']}")
                return player

        print(f"Joueur non trouvé.")
        return False

    @staticmethod
    def load_players_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Chemin du fichier non valide.")
            return []
        return data




    # def __dict__(self):
    #     return {
    #         "name": self.name,
    #         "last_name": self.last_name,
    #         "date_of_birth": self.date_of_birth,
    #         "chess_id": self.chess_id
    #     }


    # def __init__(self, name, last_name, date_of_birth, chess_id):
    #     self.name = name
    #     self.last_name = last_name
    #     self.date_of_birth = date_of_birth
    #     self.chess_id = chess_id
    #     # Ajout automatique du joueur dans la liste des joueurs players.json
    #     self.save_player(self.serialized_player())
    
    # fonction pour afficher les données d'un joueur sous forme de string. à supp si pas besoin
    # def __repr__(self):
    #     return f"{self.name} {self.last_name} {self.date_of_birth} {self.chess_id}"
    
    # fonction pour sérialiser les données d'un joueur. mettre les données dans un dictionnaire pour json
    # @staticmethod
    # def serialized_player(self):
    #     serialized_player_data = {
    #         "name": self.name,
    #         "last_name": self.last_name,
    #         "date_of_birth": self.date_of_birth,
    #         "chess_id": self.chess_id
    #     }
    #     return serialized_player_data
        
    # # @staticmethod
    # def save_player(self, player_controller):
    #     try:
    #         with open(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament\all_data\players.json", 'r') as file:
    #             data = json.load(file)
    #     except (FileNotFoundError, json.JSONDecodeError):
    #         data = []

    #     player = player_controller.create_player()
    #     data.append(asdict(player))

    #     with open('players.json', 'w') as file:
    #         json.dump(data, file)