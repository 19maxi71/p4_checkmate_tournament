import sys
sys.path.append(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament")
# import json
from all_models.tournament import Tournament
from all_views.tournament_view import TournamentView
from all_models.player import Player
from all_controllers.player_controller import PlayerController
from all_views.player_view import PlayerView
from all_models.round import Round
from all_controllers.round_controller import RoundController
from datetime import datetime
from all_models.match import Match


class TournamentController:
    
    def __init__(self):
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()
    # fonction pour créer un tournoi
    
    def create_tournament(self):
        name, location, start_date, end_date, total_players, num_rounds, description = self.tournament_view.get_tournament_details()
        self.tournament = Tournament(name, location, start_date, end_date, total_players, num_rounds, description)
        # ajout automatique des joueurs au tournoi selon la quantité total_players
        # for _ in range(int(self.tournament.total_players)):
        self.add_players_to_tournament()
            
    def load_players_to_tournament_from_file(self):
        file_path = self.player_view.get_file_path()
        players = Player.load_players_from_file(file_path)
        # self.tournament.add_player(player_data)
        for player_data in players:
            if self.is_tournament_full():
                break
            self.tournament.add_player(player_data)
            
    def add_players_to_tournament(self):
        while True:
            if self.is_tournament_full():
                break
            choice = self.tournament_view.input_players()
            # si le choix est 1, on vérifie si le joueur existe dans player et player view
            if choice == "1":
                chess_id = self.player_view.get_player_chess_id()
                player_data = {"chess_id": chess_id}
                
                player = Player.player_exists(player_data)
                if player:  # check si player n'est pas False
                    print(player)
                    self.tournament.add_player(player)
                    print("Joueur ajouté au tournoi")
                else:
                    print("Joueur non trouvé")
                # if Player.player_exists(player_data) == True:
                #     print(player)
                #     self.tournament.add_player(player_data)
                #     print("Joueur ajouté au tournoi")
                # else:
                #     print("Joueur non trouvé")
            # fo faire pareil pour les autres choix 
            elif choice == "2":
                player_controller = PlayerController()
                new_player = player_controller.create_player()
                player_controller.save_player(new_player)
                self.tournament.add_player(new_player.serialized_player())
            elif choice == "3":
                self.load_players_to_tournament_from_file()
            else:
                print("Choix invalide")
        
    def save_tournament_data_to_folder(self):
        pass
    
    # method qui check si la quantité de joueurs est atteinte
    def is_tournament_full(self):
        if len(self.tournament.players) >= int(self.tournament.total_players):
            print("Le tournoi est complet. Impossible d'ajouter plus de joueurs.")
            return True
        return False
    
    def run_rounds(self):
        for i in range(int(self.tournament.num_rounds)):
            round = Round("Round " + str(i + 1), datetime.now(), None)
            round_controller = RoundController(round)
            round_controller.generate_pairings(self.tournament.players)
            for match in round_controller.round.matches:
                match.get_match_result()
                match.get_players_points()
            round_controller.round.end_datetime = datetime.now()
            self.tournament.add_round(round_controller.round)
        self.tournament.tournament_to_json()

test = TournamentController()
test.create_tournament()
test.run_rounds()

# print(len(test.tournament.players))
# for player in range(int(test.tournament.total_players)):
#     test.add_players_to_tournament()

# print(f'il est là le jouer: {test.tournament.players}')
# print(f'dans le tournoi: {test.tournament.name}')