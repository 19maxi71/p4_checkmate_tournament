import sys
import os
# Relative path
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

import json
from dataclasses import dataclass, asdict, field
from all_models.player import Player
# from all_controllers.tournament_controller import TournamentController
from all_models.round import Round
from datetime import datetime


class Tournament: 
    def __init__(self, name, location, start_date, end_date,total_players, num_rounds, description):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = num_rounds
        self.current_round = 0
        self.description = description
        self.total_players = total_players
        self.players = []
        self.rounds = []


    # l'idée est de créer à chaque création de tournoi des tours dedans
    def add_round(self, round):
        self.rounds.append(round.serialize_round())
        self.tournament_to_json()
        
    # A voir si on garde cette méthode et si append marche
    def add_player(self, player):
        # self.players.append(player.serialized_player())
        self.players.append(player)
        self.tournament_to_json()
        

        
    def tournament_to_json(self):
        tournament_data = {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date, #datetime.strptime(self.start_date, "%d/%m/%Y").isoformat() if self.start_date else None,
            "end_date": self.end_date, #datetime.strptime(self.end_date, "%d/%m/%Y").isoformat() if self.end_date else None,
            "num_rounds": self.num_rounds,
            "current_round": self.current_round,
            "description": self.description,
            "players": [asdict(player) for player in self.players],
            "rounds": [asdict(round) for round in self.rounds]
        }
        with open(os.path.join(project_dir, 'all_data', f'{self.name}.json'), 'w') as file:
            json.dump(tournament_data, file)

    


# player = Player("John", "Doe", "2024-09-01", "66666")
# test = Tournament("Tournoi test", "Paris", "2024-09-01", "2024-09-10", 5, "Tournoi de test")
# test.add_player(player)
# print(test.players)


    # # A voir avec Driss ce qu'il y a définir comme fonctions. ET si on garde cette méthode
    # def generate_pairings(self, players):
    #     pass
    
    # def update_scores(self, round, results):
    #     pass
    
    # def is_tournament_over(self):
    #     pass
