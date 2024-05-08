import sys
sys.path.append(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament")
import json
from all_models.match import Match
from all_controllers.match_controller import MatchController
from all_views.match_view import MatchView
from all_models.round import Round
from all_models.player import Player
from all_views.player_view import PlayerView
from datetime import datetime
from random import shuffle
from copy import deepcopy

class RoundController:
    
    def __init__(self, round):
        self.round = round
        
    
    # def add_match_to_round(self, match):
    #     self.round.add_match(match)

    def generate_pairings(self, players):
        pairings = []

        if self.round.name == "Round 1":
            shuffle(players)
        else:
            players.sort(key=lambda player: player.points, reverse=True)

            for i in range(len(players)):
                if players[i].previous_opponents is None:
                    players[i].previous_opponents = []
                for j in range(i + 1, len(players)):
                    # Check si les joueurs n'ont pas joué l'un contre l'autre
                    if players[j].chess_id not in players[i].previous_opponents:
                        pairings.append((players[i], players[j]))
                        break

        return pairings

    # def generate_pairings(self, players):
    #     if self.round.name == "Round 1":
    #         shuffle(players)
    #     else:
    #         players.sort(key=lambda player: player.points, reverse=True)
        
    #     for i in range(len(players)):
    #         if players[i].previous_opponents is None:
    #             players[i].previous_opponents = []
    #         for j in range(i + 1, len(players)):
    #             # Check si les joueurs n'ont pas joué l'un contre l'autre
    #             if players[j].chess_id not in players[i].previous_opponents:
    #                 # match = Match(deepcopy(players[i]), deepcopy(players[j]))
    #                 match = Match(players[i], players[j])
    #                 match_controller = MatchController(match, MatchView())
    #                 match_controller.run_match()
    #                 self.round.matches.append(match)
    #                 break


    # def generate_pairings(self, players):
    #     if self.round.name == "Round 1":
    #         shuffle(players)
    #     else:
    #         players.sort(key=lambda player: player.points, reverse=True)
        
    #     for i in range(len(players)):
    #         for j in range(i + 1, len(players)):
    #             # Check if players have not played against each other
    #             if players[j].chess_id not in players[i].previous_opponents:
    #                 match = Match(players[i], players[j])
    #                 self.add_match_to_round(match)
    #                 break
            
    # def add_match(self, match):
    #     self.matches.append(match)
    # def generate_pairings(self):
    #     try:
    #         with open(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament\all_data\players.json", 'r') as file:
    #             data = json.load(file)
    #     except (FileNotFoundError, json.JSONDecodeError):
    #         data = []

    #     for i in range(0, len(data), 2):
    #         player1 = data[i]
    #         player2 = data[i + 1]
    #         match = Match(player1, player2)
    #         self.add_match(match)

# test_round = create_round("Round 1", "2024-09-01 09:00", "2024-09-01 12:00")
# test_round.generate_pairings()

# # Print tous les matchs du tour
# for match in test_round.matches:
#     print(f"{test_round.name}\n{match}")

#     # obtenir le résultat du match
#     match.get_match_result()
#     print(match.get_players_points())