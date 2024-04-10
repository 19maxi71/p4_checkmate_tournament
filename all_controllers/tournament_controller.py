import sys
sys.path.append(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament")
import json
from all_models.tournament import Tournament
from all_views.tournament_view import TournamentView
from all_models.player import Player


class TournamentController:
    
    def __init__(self):
        self.tournament_view = TournamentView()
        self.tournament = None
    # fonction pour créer un tournoi
    
    def create_tournament(self):
        name, location, start_date, end_date, num_rounds, description = self.tournament_view.get_tournament_details()
        tournament = Tournament(name, location, start_date, end_date, num_rounds, description)
        return tournament

    def add_players_to_tournament(self):
        choice = self.tournament_view.input_players()
        if choice == "1":
            self.player_exists()
        elif choice == "2":
            self.add_player()
        elif choice == "3":
            self.load_players()
        else:
            print("Choix invalide")
        
    def save_tournament_data_to_folder(self):
        pass
    
        
test = TournamentController()
test.create_tournament()
test.add_players_to_tournament()