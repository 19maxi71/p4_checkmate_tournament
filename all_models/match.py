import sys
sys.path.append(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament")
import json
from all_models.player import Player
from all_views.player_view import PlayerView

# class Match:
#     def __init__(self, player1, player2):
#         self.player1 = player1
#         self.player2 = player2
#         self.win = None
#         self.draw = None
    
#     def create_match_from_json_list(self):
#         try:
#             with open(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament\all_data\players.json", 'r') as file:
#                 data = json.load(file)
#         except (FileNotFoundError, json.JSONDecodeError):
#             data = []
#         player1 = data[-1]
#         player2 = data[-2]
#         match = Match(player1, player2)
#         return match
    
#     def get_match_result(self):
#         result = input("Entrer le résultat du match (1 pour victoire de joueur 1, 2 pour victoire de joueur 2, 0 pour match nul): ")
#         if result == '1':
#             self.win = self.player1
#         elif result == '2':
#             self.win = self.player2
#         elif result == '0':
#             self.draw = True
#         else:
#             print("Entrée invalide. Veuillez entrer 1, 2 ou 0")
#             self.get_match_result()

# test = Match()
# test.create_match_from_json_list()
# test.get_match_result()
class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.win = None
        self.draw = None

    def player_chess_id(self):
        chess_id1 = input("Entrer l'Identifian National d'Echecs du joueur 1: ")
        chess_id2 = input("Entrer l'Identifian National d'Echecs du joueur 2: ")
        return chess_id1, chess_id2

    @staticmethod
    def create_match_from_json_list(chess_id1, chess_id2):
        try:
            with open(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament\all_data\players.json", 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        player1 = None
        player2 = None
        for player in data:
            if player['chess_id'] == chess_id1:
                player1 = player
            elif player['chess_id'] == chess_id2:
                player2 = player
        if player1 is None or player2 is None:
            print("Joueur non trouvé. Veuillez vérifier l'Identifian National d'Echecs.")
            return None
        match = Match(player1, player2)
        return match

    def get_match_result(self):
        result = input("Entrer le résultat du match (1 pour victoire de joueur 1, 2 pour victoire de joueur 2, 0 pour match nul): ")
        # réflechi comment faire les points aussi!
        if result == '1':
            self.win = self.player1
            print(f"Le joueur {self.player1['name']} a gagné")
        elif result == '2':
            self.win = self.player2
            print(f"Le joueur {self.player2['name']} a gagné")
        elif result == '0':
            self.draw = True
            print("Match nul")
        else:
            print("Entrée invalide. Veuillez entrer 1, 2 ou 0")
            self.get_match_result()

# on doit créer un objet de match pour pouvoir appeler les méthodes
test_match = Match(None, None)

# pour obtenir les id des joueurs
chess_id1, chess_id2 = test_match.player_chess_id()

# Créer le match
test = Match.create_match_from_json_list(chess_id1, chess_id2)

# obtenir le résultat du match
test.get_match_result()
