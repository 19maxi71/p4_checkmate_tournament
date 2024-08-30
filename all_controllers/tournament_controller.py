import sys
import os
from datetime import datetime
from all_models.tournament import Tournament
from all_views.tournament_view import TournamentView
from all_models.player import Player
from all_controllers.player_controller import PlayerController
from all_views.player_view import PlayerView
from all_models.round import Round
from all_controllers.round_controller import RoundController
from all_models.match import Match
from all_controllers.match_controller import MatchController
from all_views.match_view import MatchView
from copy import deepcopy

# Relative path
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

class TournamentController:
    
    def __init__(self):
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()
    
    def create_tournament(self):
        name, location, start_date, end_date, total_players, num_rounds, description = self.tournament_view.get_tournament_details()
        self.tournament = Tournament(name, location, start_date, end_date, total_players, num_rounds, description)
        self.add_players_to_tournament()
            
    def load_players_to_tournament_from_file(self):
        file_path = self.player_view.get_file_path()
        players = Player.load_players_from_file(file_path)
        for player_data in players:
            if self.is_tournament_full():
                break
            player = Player(**player_data)
            self.tournament.add_player(player)
            
    def add_players_to_tournament(self):
        while True:
            if self.is_tournament_full():
                break
            choice = self.tournament_view.input_players()
            if choice == "1":
                chess_id = self.player_view.get_player_chess_id()
                player_data = {"chess_id": chess_id}
                player = Player.player_exists(player_data)
                if player:
                    self.tournament.add_player(Player(**player))
                    print("Joueur ajouté au tournoi")
                else:
                    print("Joueur non trouvé")
            elif choice == "2":
                player_controller = PlayerController()
                new_player = player_controller.create_player()
                self.tournament.add_player(new_player)
            elif choice == "3":
                self.load_players_to_tournament_from_file()
            else:
                print("Choix invalide")
        
    def save_tournament_data_to_folder(self):
        pass
    
    def is_tournament_full(self):
        if len(self.tournament.players) >= int(self.tournament.total_players):
            print("Le tournoi est complet. Impossible d'ajouter plus de joueurs.")
            return True
        return False
    
    def run_rounds(self):
        for i in range(int(self.tournament.num_rounds)):
            round = Round("Round " + str(i + 1), str(datetime.now()), None)
            round_controller = RoundController(round)
            pairings = round_controller.generate_pairings(self.tournament.players)

            if not pairings:
                print(f"All possible pairings have been exhausted by Round {i + 1}.")
                break

            for player1, player2 in pairings:
                match = Match(deepcopy(player1), deepcopy(player2))
                match_controller = MatchController(match, MatchView())
                updated_player1, updated_player2 = match_controller.run_match()

                # Stocker les points des joueurs dans le match séparément
                match.player1.points = updated_player1.points - player1.points
                match.player2.points = updated_player2.points - player2.points

                round.matches.append(match)

                # Maj des scores des joueurs et des adversaires précédents dans la liste du tournoi
                for tournament_player in self.tournament.players:
                    if tournament_player.chess_id == updated_player1.chess_id:
                        tournament_player.points = updated_player1.points
                        if updated_player2.chess_id not in tournament_player.previous_opponents:
                            tournament_player.previous_opponents.append(updated_player2.chess_id)
                    elif tournament_player.chess_id == updated_player2.chess_id:
                        tournament_player.points = updated_player2.points
                        if updated_player1.chess_id not in tournament_player.previous_opponents:
                            tournament_player.previous_opponents.append(updated_player1.chess_id)

            round.end_datetime = str(datetime.now())
            self.tournament.rounds.append(round)

        self.tournament.tournament_to_json()

# start le tournoi
if __name__ == "__main__":
    test = TournamentController()
    test.create_tournament()
    test.run_rounds()














# # import json
# from all_models.tournament import Tournament
# from all_views.tournament_view import TournamentView
# from all_models.player import Player
# from all_controllers.player_controller import PlayerController
# from all_views.player_view import PlayerView
# from all_models.round import Round
# from all_controllers.round_controller import RoundController
# from datetime import datetime
# from all_models.match import Match
# from all_controllers.match_controller import MatchController
# from all_views.match_view import MatchView

# class TournamentController:
    
#     def __init__(self):
#         self.tournament_view = TournamentView()
#         self.player_view = PlayerView()
#     # fonction pour créer un tournoi
    
#     def create_tournament(self):
#         name, location, start_date, end_date, total_players, num_rounds, description = self.tournament_view.get_tournament_details()
#         self.tournament = Tournament(name, location, start_date, end_date, total_players, num_rounds, description)
#         # ajout automatique des joueurs au tournoi selon la quantité total_players
#         # for _ in range(int(self.tournament.total_players)):
#         self.add_players_to_tournament()
            
#     def load_players_to_tournament_from_file(self):
#         file_path = self.player_view.get_file_path()
#         players = Player.load_players_from_file(file_path)
#         # self.tournament.add_player(player_data)
#         for player_data in players:
#             if self.is_tournament_full():
#                 break
#             player = Player(**player_data)
#             self.tournament.add_player(player)
    
#     # def add_player_to_tournament(self, player_dict):
#     #     player = Player(**player_dict)
#     #     self.tournament.add_player(player)
            
#     def add_players_to_tournament(self):
#         while True:
#             if self.is_tournament_full():
#                 break
#             choice = self.tournament_view.input_players()
#             # si le choix est 1, on vérifie si le joueur existe dans player et player view
#             if choice == "1":
#                 chess_id = self.player_view.get_player_chess_id()
#                 player_data = {"chess_id": chess_id}
                
#                 player = Player.player_exists(player_data)
#                 if player:  # check si player n'est pas False
#                     print(player)
#                     self.tournament.add_player(Player(**player))  # Ensure player is a Player instance
#                     print("Joueur ajouté au tournoi")
#                 else:
#                     print("Joueur non trouvé")
#             # si le choix est 2, on crée un nouveau joueur
#             elif choice == "2":
#                 player_controller = PlayerController()
#                 new_player = player_controller.create_player()
#                 # player_controller.save_player(new_player)
#                 self.tournament.add_player(new_player)
#             elif choice == "3":
#                 self.load_players_to_tournament_from_file()
#             else:
#                 print("Choix invalide")
        
#     def save_tournament_data_to_folder(self):
#         pass
    
#     # method qui check si la quantité de joueurs est atteinte
#     def is_tournament_full(self):
#         if len(self.tournament.players) >= int(self.tournament.total_players):
#             print("Le tournoi est complet. Impossible d'ajouter plus de joueurs.")
#             return True
#         return False
    
#     def run_rounds(self):
#         for i in range(int(self.tournament.num_rounds)):
#             round = Round("Round " + str(i + 1), str(datetime.now()), None)
#             round_controller = RoundController(round)
#             pairings = round_controller.generate_pairings(self.tournament.players)

#             for player1, player2 in pairings:
#                 match = Match(player1, player2)
#                 match_controller = MatchController(match, MatchView())
#                 updated_player1, updated_player2 = match_controller.run_match()
#                 round.matches.append(match)

#                 # Update the players' scores and previous opponents in the tournament list
#                 for tournament_player in self.tournament.players:
#                     if tournament_player.chess_id == updated_player1.chess_id:
#                         tournament_player.points += updated_player1.points
#                         if updated_player2.chess_id not in tournament_player.previous_opponents:
#                             tournament_player.previous_opponents.append(updated_player2.chess_id)
#                     elif tournament_player.chess_id == updated_player2.chess_id:
#                         tournament_player.points += updated_player2.points
#                         if updated_player1.chess_id not in tournament_player.previous_opponents:
#                             tournament_player.previous_opponents.append(updated_player1.chess_id)

#             round.end_datetime = str(datetime.now())
#             self.tournament.rounds.append(round)

#         self.tournament.tournament_to_json()
        


# test = TournamentController()
# test.create_tournament()
# test.run_rounds()










# print(len(test.tournament.players))
# for player in range(int(test.tournament.total_players)):
#     test.add_players_to_tournament()

# print(f'il est là le jouer: {test.tournament.players}')
# print(f'dans le tournoi: {test.tournament.name}')



    # def run_rounds(self):
    #     for i in range(int(self.tournament.num_rounds)):
    #         round = Round("Round " + str(i + 1), str(datetime.now()), None)
    #         round_controller = RoundController(round)
    #         pairings = round_controller.generate_pairings(self.tournament.players)

    #         for player1, player2 in pairings:
    #             match = Match(player1, player2)
    #             match_controller = MatchController(match, MatchView())
    #             match_controller.run_match()
    #             round.matches.append(match)

    #             # # update joueur dans le tournoi avec les points et les adversaires précédents
    #             # for tournament_player in self.tournament.players:
    #             #     if tournament_player.chess_id == player1.chess_id:
    #             #         tournament_player.points = player1.points
    #             #         tournament_player.previous_opponents = player1.previous_opponents
    #             #     elif tournament_player.chess_id == player2.chess_id:
    #             #         tournament_player.points = player2.points
    #             #         tournament_player.previous_opponents = player2.previous_opponents

    #         round.end_datetime = str(datetime.now())
    #         self.tournament.rounds.append(round)

    #     self.tournament.tournament_to_json()
    

# D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament\all_data\players.json