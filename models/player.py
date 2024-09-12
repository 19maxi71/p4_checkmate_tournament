import sys
import os
import json
from dataclasses import dataclass, asdict, field
from typing import Optional, List

# Chemin relatif
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
        """Convertit l'objet Player en dictionnaire."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        """Crée une instance de Player à partir d'un dictionnaire."""
        return cls(
            name=data["name"],
            last_name=data["last_name"],
            date_of_birth=data["date_of_birth"],
            chess_id=data["chess_id"],
            points=data.get("points", 0.0),
            previous_opponents=data.get("previous_opponents", []),
        )

    @staticmethod
    def player_exists(player_data):
        """Vérifie si un joueur existe déjà dans le fichier JSON."""
        try:
            players_data_file_path = os.path.join(
                project_dir, "data", "players.json"
            )
            with open(players_data_file_path, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("ouvre pas ton json machine")  # voir si l'erreur est là
            return False

        for player in data:
            if player["chess_id"] == player_data["chess_id"]:
                print(f"Joueur trouvé: {player['name']} {player['last_name']}")
                return player

        print(f"Joueur non trouvé.")
        return False

    @staticmethod
    def load_players_from_file(file_path):
        """Charge les joueurs à partir d'un fichier JSON."""
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Chemin du fichier non valide.")
            return []
        return data
