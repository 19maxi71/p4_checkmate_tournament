import sys
sys.path.append(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament")
import json
from all_models.match import Match
# from all_models.player import Player
# from all_views.player_view import PlayerView

class Round:
    
    def __init__(self, name, start_datetime, end_datetime):
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = []
    
    def add_match(self, match):
        self.matches.append(match)
        
#     def generate_pairings(self):
#         try:
#             with open(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament\all_data\players.json", 'r') as file:
#                 data = json.load(file)
#         except (FileNotFoundError, json.JSONDecodeError):
#             data = []

#         for i in range(0, len(data), 2):
#             player1 = data[i]
#             player2 = data[i + 1]
#             pair = (player1['chess_id'], player2['chess_id'])
#             self.add_match(pair)

# test_round = Round("Tour 1", "2024-09-01 09:00", "2024-09-01 18:00")
# test_round.generate_pairings()

# # Print tous les matchs du tour
# for match in test_round.matches:
#     print(f"{test_round.name}\n{match}")
        
#     # on doit créer un objet de match pour pouvoir appeler les méthodes
#     match = Match(None, None)

#     # pour obtenir les id des joueurs
#     chess_id1, chess_id2 = match.player_chess_id()

#     # Créer le match
#     match_of_round = Match.create_match_for_round(chess_id1, chess_id2)

#     # obtenir le résultat du match
#     match_of_round.get_players_points()
#     print(match_of_round.get_players_points())

    def generate_pairings(self):
        try:
            with open(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament\all_data\players.json", 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        for i in range(0, len(data), 2):
            player1 = data[i]
            player2 = data[i + 1]
            match = Match(player1, player2)
            self.add_match(match)

test_round = Round("Tour 1", "2024-09-01 09:00", "2024-09-01 18:00")
test_round.generate_pairings()

# Print tous les matchs du tour
for match in test_round.matches:
    print(f"{test_round.name}\n{match}")

    # obtenir le résultat du match
    match.get_match_result()
    print(match.get_players_points())