import sys
sys.path.append(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament")
import json
from all_models.tournament import Tournament
from all_views.tournament_view import TournamentView


class TournamentController:
    
    def __init__(self):
        self.tournament_view = TournamentView()
    # fonction pour créer un tournoi
    
    def create_tournament(self):
        name, location, start_date, end_date, num_rounds, description = self.tournament_view.get_tournament_details()
        tournament = Tournament(name, location, start_date, end_date, num_rounds, description)
        return tournament

    
    
        
test = TournamentController()
testtest = test.create_tournament()
print(testtest)