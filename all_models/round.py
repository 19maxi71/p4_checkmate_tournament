import sys
sys.path.append(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament")
# import json
from all_models.match import Match
# from all_models.player import Player
# from all_views.player_view import PlayerView

class Round:
    
    def __init__(self, name, start_datetime, end_datetime):
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = []

    def serialize_round(self):
        return {
            "name": self.name,
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": self.end_datetime.isoformat() if self.end_datetime else None,
            "matches": [match.serialize_match() for match in self.matches]
        }

    def add_match(self, match):
        self.matches.append(match)

    def add_round(self, round):
        self.rounds.append(round.serialize_round())
        self.tournament_to_json()

#     def generate_pairings(self):
#         try:
#             with open(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament\all_data\players.json", 'r') as file:
#                 data = json.load(file)
#         except (FileNotFoundError, json.JSONDecodeError):
#             data = []

#         for i in range(0, len(data), 2):
#             player1 = data[i]
#             player2 = data[i + 1]
#             match = Match(player1, player2)
#             self.add_match(match)

# test_round = create_round("Round 1", "2024-09-01 09:00", "2024-09-01 12:00")
# test_round.generate_pairings()

# # Print tous les matchs du tour
# for match in test_round.matches:
#     print(f"{test_round.name}\n{match}")

#     # obtenir le résultat du match
#     match.get_match_result()
#     print(match.get_players_points())