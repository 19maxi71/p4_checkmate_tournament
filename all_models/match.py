import sys
import os
# Relative path
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

import json
from dataclasses import dataclass, asdict, field
from typing import Optional, List
from all_models.player import Player



@dataclass
class Match:
    player1: Player
    player2: Player
    result: str = None

    @classmethod
    def from_dict(cls, data):
        return cls(
            player1=Player.from_dict(data.get('player1')),
            player2=Player.from_dict(data.get('player2')),
            result=data.get('result', None)
        )











































# class Match:
#     def __init__(self, player1, player2):
#         self.player1 = player1
#         self.player2 = player2
#         self.win = None
#         self.draw = None
#         self.result = None

#     def serialize_match(self):
#         return {
#             "player1": self.player1,
#             "player2": self.player2,
#             "result": self.result
#         }

#     # @staticmethod    
#     # def create_match_for_round(chess_id1, chess_id2):
#     #     try:
#     #         with open(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament\all_data\players.json", 'r') as file:
#     #             data = json.load(file)
#     #     except (FileNotFoundError, json.JSONDecodeError):
#     #         data = []
#     #     player1 = None
#     #     player2 = None
#     #     for player in data:
#     #         if player['chess_id'] == chess_id1:
#     #             player1 = player
#     #         elif player['chess_id'] == chess_id2:
#     #             player2 = player
#     #     if player1 is None or player2 is None:
#     #         print("Joueur non trouvé. Veuillez vérifier l'Identifian National d'Echecs.")
#     #         return None
#     #     match = Match(player1, player2)
#     #     return match    
        
    
    

#     def get_match_result(self):
#         if self.result is None:
#             self.result = input("Entrer le résultat du match (1 pour victoire de joueur 1, 2 pour victoire de joueur 2, 0 pour match nul): ")
#             # réflechi comment faire les points aussi!
#             if self.result == '1':
#                 self.win = self.player1
#                 print(f"Le joueur {self.player1['name']} a gagné")
#             elif self.result == '2':
#                 self.win = self.player2
#                 print(f"Le joueur {self.player2['name']} a gagné")
#             elif self.result == '0':
#                 self.draw = True
#                 print("Match nul")
#             else:
#                 print("Entrée invalide.")
#                 self.get_match_result()
#         return self.result

#     def get_players_points(self):
#         result_of_match = self.get_match_result()
#         # deep copy, la copie player1 mais qui ne se change pas si on change player1 
#         player1_copy = self.player1.copy()
#         player2_copy = self.player2.copy()
#         if result_of_match == '1':
#             player1_copy['points'] = 1
#             player2_copy['points'] = 0
#         elif result_of_match == '2':
#             player2_copy['points'] = 1
#             player1_copy['points'] = 0
#         elif result_of_match == '0':
#             player1_copy['points'] = 0.5
#             player2_copy['points'] = 0.5
#         print(f'Le joueur {player1_copy["name"]} obtient {player1_copy["points"]} points\n'
#             f'Le joueur {player2_copy["name"]} obtient {player2_copy["points"]} points')
#         return ([self.player1, player1_copy['points']], [self.player2, player2_copy['points']])
    
#     def __str__(self):
#         return f"Match entre {self.player1['name']} et {self.player2['name']}"
    
# # # on doit créer un objet de match pour pouvoir appeler les méthodes
# # test_match = Match(None, None)

# # # pour obtenir les id des joueurs
# # chess_id1, chess_id2 = test_match.player_chess_id()

# # # Créer le match
# # test = Match.create_match_for_round(chess_id1, chess_id2)

# # # obtenir le résultat du match
# # test.get_players_points()
# # print(test.get_players_points())
