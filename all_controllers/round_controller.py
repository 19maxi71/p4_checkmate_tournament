import sys
import os
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

# Relative path
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

class RoundController:
    def __init__(self, round):
        self.round = round

    def generate_pairings(self, players):
        pairings = []
        players_sorted = sorted(players, key=lambda x: x.points, reverse=True)
        
        while len(players_sorted) > 1:
            player1 = players_sorted.pop(0)
            for i, player2 in enumerate(players_sorted):
                if player2.chess_id not in player1.previous_opponents:
                    pairings.append((player1, player2))
                    players_sorted.pop(i)
                    break
            else:
                # si trouve pas d'adversaire, on prend le premier joueur restant
                player2 = players_sorted.pop(0)
                pairings.append((player1, player2))
        
        return pairings











# class RoundController:
    
#     def __init__(self, round):
#         self.round = round

#     def generate_pairings(self, players):
#         pairings = []

#         if self.round.name == "Round 1":
#             shuffle(players)
#             for i in range(0, len(players), 2):
#                 if i + 1 < len(players):
#                     pairings.append((players[i], players[i + 1]))
#         else:
#             players.sort(key=lambda player: player.points, reverse=True)
#             used_players = set()

#             for i in range(len(players)):
#                 if players[i].chess_id in used_players:
#                     continue
#                 if players[i].previous_opponents is None:
#                     players[i].previous_opponents = []
#                 for j in range(i + 1, len(players)):
#                     if players[j].chess_id in used_players:
#                         continue
#                     if players[j].chess_id not in players[i].previous_opponents:
#                         pairings.append((players[i], players[j]))
#                         used_players.add(players[i].chess_id)
#                         used_players.add(players[j].chess_id)
#                         break

#         return pairings











# import sys
# import os
# # Relative path
# current_dir = os.path.dirname(__file__)
# project_dir = os.path.dirname(current_dir)
# sys.path.append(project_dir)

# import json
# from all_models.match import Match
# from all_controllers.match_controller import MatchController
# from all_views.match_view import MatchView
# from all_models.round import Round
# from all_models.player import Player
# from all_views.player_view import PlayerView
# from datetime import datetime
# from random import shuffle
# from copy import deepcopy

# class RoundController:
    
#     def __init__(self, round):
#         self.round = round
        
    
#     # def add_match_to_round(self, match):
#     #     self.round.add_match(match)

#     def generate_pairings(self, players):
#         pairings = []

#         if self.round.name == "Round 1":
#             shuffle(players)
#         else:
#             players.sort(key=lambda player: player.points, reverse=True)

#             for i in range(len(players)):
#                 if players[i].previous_opponents is None:
#                     players[i].previous_opponents = []
#                 for j in range(i + 1, len(players)):
#                     # Check si les joueurs n'ont pas joué l'un contre l'autre
#                     if players[j].chess_id not in players[i].previous_opponents:
#                         pairings.append((players[i], players[j]))
#                         break

#         return pairings






















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