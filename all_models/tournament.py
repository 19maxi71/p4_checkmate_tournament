import sys
sys.path.append(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament")
import json
# from all_models.player import Player
# from all_controllers.tournament_controller import TournamentController


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

    # A voir si on garde cette méthode et si append marche
    def add_player(self, player):
        self.players.append(player)
        self.tournament_to_json()
        
    def tournament_to_json(self):
        tournament_data = {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "num_rounds": self.num_rounds,
            "current_round": self.current_round,
            "description": self.description,
            "players": self.players,  # maj la liste des joueurs. Voir __dict__ dans player.py qu'on rajouté sinon marchera pas
            "rounds": self.rounds
        }
        with open(f'D:\\All OpenClassRooms projects\\p4_checkmate_tournament\\p4_checkmate_tournament\\all_data\\{self.name}.json', 'w') as file:
            json.dump(tournament_data, file)

    # A voir avec Driss ce qu'il y a définir comme fonctions. ET si on garde cette méthode
    def generate_pairings(self, players):
        pass
    
    def update_scores(self, round, results):
        pass
    
    def is_tournament_over(self):
        pass

# player = Player("John", "Doe", "2024-09-01", "66666")
# test = Tournament("Tournoi test", "Paris", "2024-09-01", "2024-09-10", 5, "Tournoi de test")
# test.add_player(player)
# print(test.players)