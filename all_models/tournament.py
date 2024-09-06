from dataclasses import dataclass, asdict, field
from typing import List
import os
import json
import sys

# Relative path
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

from all_models.player import Player
from all_models.round import Round

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
        self.rounds.append(round)
        self.tournament_to_json()

    def add_player(self, player):
        self.players.append(player)
        self.tournament_to_json()

    def tournament_to_json(self):
        tournament_data = asdict(self)
        with open(os.path.join(project_dir, 'all_data', f'{self.name}.json'), 'w') as file:
            json.dump(tournament_data, file, indent=4)

    @classmethod
    def from_dict(cls, data):
        tournament = cls(
            name=data.get('name', 'Unknown Tournament'),
            location=data.get('location', 'Unknown Location'),
            start_date=data.get('start_date', 'Unknown Start Date'),
            end_date=data.get('end_date', 'Unknown End Date'),
            total_players=data.get('total_players', 0),
            num_rounds=data.get('num_rounds', 0),
            description=data.get('description', '')
        )
        tournament.players = [Player.from_dict(player_data) for player_data in data.get('players', [])]
        tournament.rounds = [Round.from_dict(round_data) for round_data in data.get('rounds', [])]
        return tournament

    @classmethod
    def load_from_json(cls, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            return cls.from_dict(data)


















# import sys
# import os
# import json
# from dataclasses import dataclass, asdict, field
# from typing import List
# from all_models.player import Player
# from all_models.round import Round

# # Relative path
# current_dir = os.path.dirname(__file__)
# project_dir = os.path.dirname(current_dir)
# sys.path.append(project_dir)

# @dataclass
# class Tournament:
#     name: str
#     location: str
#     start_date: str
#     end_date: str
#     total_players: int
#     num_rounds: int
#     description: str
#     current_round: int = 0
#     players: List[Player] = field(default_factory=list)
#     rounds: List[Round] = field(default_factory=list)

#     def add_round(self, round):
#         self.rounds.append(round)
#         self.tournament_to_json()

#     def add_player(self, player):
#         self.players.append(player)
#         self.tournament_to_json()

#     def tournament_to_json(self):
#         tournament_data = asdict(self)
#         with open(os.path.join(project_dir, 'all_data', f'{self.name}.json'), 'w') as file:
#             json.dump(tournament_data, file, indent=4)

#     @classmethod
#     def from_dict(cls, data):
#         tournament = cls(
#             name=data.get('name', 'Unknown Tournament'),
#             location=data.get('location', 'Unknown Location'),
#             start_date=data.get('start_date', 'Unknown Start Date'),
#             end_date=data.get('end_date', 'Unknown End Date'),
#             total_players=data.get('total_players', 0),
#             num_rounds=data.get('num_rounds', 0),
#             description=data.get('description', '')
#         )
#         tournament.players = [Player.from_dict(player_data) for player_data in data.get('players', [])]
#         tournament.rounds = [Round.from_dict(round_data) for round_data in data.get('rounds', [])]
#         return tournament



















# import sys
# import os
# # Relative path
# current_dir = os.path.dirname(__file__)
# project_dir = os.path.dirname(current_dir)
# sys.path.append(project_dir)

# import json
# from dataclasses import dataclass, asdict, field
# from all_models.player import Player
# # from all_controllers.tournament_controller import TournamentController
# from all_models.round import Round
# from datetime import datetime


# class Tournament: 
#     def __init__(self, name, location, start_date, end_date,total_players, num_rounds, description):
#         self.name = name
#         self.location = location
#         self.start_date = start_date
#         self.end_date = end_date
#         self.num_rounds = num_rounds
#         self.current_round = 0
#         self.description = description
#         self.total_players = total_players
#         self.players = []
#         self.rounds = []


#     # l'idée est de créer à chaque création de tournoi des tours dedans
#     def add_round(self, round):
#         self.rounds.append(round.serialize_round())
#         self.tournament_to_json()
        
#     # A voir si on garde cette méthode et si append marche
#     def add_player(self, player):
#         # self.players.append(player.serialized_player())
#         self.players.append(player)
#         self.tournament_to_json()
        

        
#     def tournament_to_json(self):
#         tournament_data = {
#             "name": self.name,
#             "location": self.location,
#             "start_date": self.start_date, #datetime.strptime(self.start_date, "%d/%m/%Y").isoformat() if self.start_date else None,
#             "end_date": self.end_date, #datetime.strptime(self.end_date, "%d/%m/%Y").isoformat() if self.end_date else None,
#             "num_rounds": self.num_rounds,
#             "current_round": self.current_round,
#             "description": self.description,
#             "players": [asdict(player) for player in self.players],
#             "rounds": [asdict(round) for round in self.rounds]
#         }
#         with open(os.path.join(project_dir, 'all_data', f'{self.name}.json'), 'w') as file:
#             json.dump(tournament_data, file)
