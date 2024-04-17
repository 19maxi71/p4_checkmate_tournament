import sys
sys.path.append(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament")
# import json
from all_models.tournament import Tournament
from all_views.tournament_view import TournamentView
from all_models.player import Player
from all_views.player_view import PlayerView


class TournamentController:
    
    def __init__(self):
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()
    # fonction pour créer un tournoi
    
    def create_tournament(self):
        name, location, start_date, end_date, total_players, num_rounds, description = self.tournament_view.get_tournament_details()
        self.tournament = Tournament(name, location, start_date, end_date, total_players, num_rounds, description)
        # ajout automatique des joueurs au tournoi selon la quantité total_players
        for _ in range(int(self.tournament.total_players)):
            self.add_players_to_tournament()

    def add_players_to_tournament(self):
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
            Tournament.add_player()
        elif choice == "3":
            Player.load_players()
        else:
            print("Choix invalide")
        
    def save_tournament_data_to_folder(self):
        pass
    
        
test = TournamentController()
test.create_tournament()
print(len(test.tournament.players))
# for player in range(int(test.tournament.total_players)):
#     test.add_players_to_tournament()

# print(f'il est là le jouer: {test.tournament.players}')
# print(f'dans le tournoi: {test.tournament.name}')