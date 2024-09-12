from dataclasses import dataclass, asdict, field
from typing import List
import os
import json
import sys

# Chemin relatif
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

from models.player import Player
from models.round import Round
<<<<<<< HEAD

=======
>>>>>>> 80fdfa0 (Refactor file and folder names)


@dataclass
class Tournament:
    name: str
    location: str
    start_date: str
    end_date: str
    total_players: int
    num_rounds: int
    description: str
    current_round: int = 0
    players: List[Player] = field(default_factory=list)
    rounds: List[Round] = field(default_factory=list)

    def add_round(self, round):
        """Ajoute un round au tournoi et sauvegarde l'état actuel dans un fichier JSON."""
        self.rounds.append(round)
        self.tournament_to_json()

    def add_player(self, player):
        """Ajoute un joueur au tournoi et sauvegarde l'état actuel dans un fichier JSON."""
        self.players.append(player)
        self.tournament_to_json()

    def tournament_to_json(self):
        """Sauvegarde l'état actuel du tournoi dans un fichier JSON."""
        tournament_data = asdict(self)
        with open(
<<<<<<< HEAD
<<<<<<< HEAD:models/tournament.py
            os.path.join(project_dir, "data", f"{self.name}.json"), "w"
=======
            os.path.join(project_dir, "all_data", f"{self.name}.json"), "w"
>>>>>>> 3d2a1fe (modif readme.md):all_models/tournament.py
=======
            os.path.join(project_dir, "data", f"{self.name}.json"), "w"
>>>>>>> 80fdfa0 (Refactor file and folder names)
        ) as file:
            json.dump(tournament_data, file, indent=4)

    @classmethod
    def from_dict(cls, data):
        """Crée une instance de Tournament à partir d'un dictionnaire."""
        tournament = cls(
            name=data.get("name", "Unknown Tournament"),
            location=data.get("location", "Unknown Location"),
            start_date=data.get("start_date", "Unknown Start Date"),
            end_date=data.get("end_date", "Unknown End Date"),
            total_players=data.get("total_players", 0),
            num_rounds=data.get("num_rounds", 0),
            description=data.get("description", ""),
        )
        tournament.players = [
            Player.from_dict(player_data) for player_data in data.get("players", [])
        ]
        tournament.rounds = [
            Round.from_dict(round_data) for round_data in data.get("rounds", [])
        ]
        return tournament

    @classmethod
    def load_from_json(cls, file_path):
        """Charge un tournoi à partir d'un fichier JSON."""
        with open(file_path, "r") as file:
            data = json.load(file)
            return cls.from_dict(data)
