import sys
sys.path.append(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament")
from dataclasses import asdict

from all_views.match_view import MatchView
from all_models.match import Match

from all_controllers.player_controller import PlayerController
from copy import deepcopy

class MatchController:
    def __init__(self, match, match_view):
        self.match = match
        self.match_view = match_view


    def run_match(self):
        self.get_match_result()
        self.get_players_points_and_opponent_chess_id()  # Call your method to assign points and opponents
        self.match_view.display_match_result(self.match)
        
    def get_players_points_and_opponent_chess_id(self):
        result_of_match = self.get_match_result()

        if result_of_match == '1':
            self.match.player1.points += 1
            self.match.player2.points += 0
        elif result_of_match == '2':
            self.match.player2.points += 1
            self.match.player1.points += 0
        elif result_of_match == '0':
            self.match.player1.points += 0.5
            self.match.player2.points += 0.5

        # Initialize previous opponents list if it doesn't exist
        if self.match.player1.previous_opponents is None:
            self.match.player1.previous_opponents = []
        if self.match.player2.previous_opponents is None:
            self.match.player2.previous_opponents = []

        # Add opponent's chess_id to previous opponents list
        self.match.player1.previous_opponents.append(self.match.player2.chess_id)
        self.match.player2.previous_opponents.append(self.match.player1.chess_id)


    def get_match_result(self):
        if self.match.result is None:
            self.match.result = self.match_view.input_match_result(self.match)
        return self.match.result

    # def get_players_points_and_opponent_chess_id(self):
    #     result_of_match = self.get_match_result()

    #     # Create deep copies of the players
    #     player1_copy = deepcopy(self.match.player1)
    #     player2_copy = deepcopy(self.match.player2)

    #     if result_of_match == '1':
    #         player1_copy.points = 1
    #         player2_copy.points = 0
    #     elif result_of_match == '2':
    #         player2_copy.points = 1
    #         player1_copy.points = 0
    #     elif result_of_match == '0':
    #         player1_copy.points = 0.5
    #         player2_copy.points = 0.5

    #     # Initialize previous opponents list if it doesn't exist
    #     if player1_copy.previous_opponents is None:
    #         player1_copy.previous_opponents = []
    #     if player2_copy.previous_opponents is None:
    #         player2_copy.previous_opponents = []

    #     # Add opponent's chess_id to previous opponents list
    #     player1_copy.previous_opponents.append(player2_copy.chess_id)
    #     player2_copy.previous_opponents.append(player1_copy.chess_id)

        # return ([asdict(player1_copy), player1_copy.points], [asdict(player2_copy), player2_copy.points])

    # def get_players_points_and_opponent_chess_id(self):
    #     result_of_match = self.get_match_result()
    #     if result_of_match == '1':
    #         self.match.player1.points = 1
    #         self.match.player2.points = 0
    #     elif result_of_match == '2':
    #         self.match.player2.points = 1
    #         self.match.player1.points = 0
    #     elif result_of_match == '0':
    #         self.match.player1.points = 0.5
    #         self.match.player2.points = 0.5
        
    #     # Initialisation de la liste des adversaires précédents si elle n'existe pas
    #     if self.match.player1.previous_opponents is None:
    #         self.match.player1.previous_opponents = []
    #     if self.match.player2.previous_opponents is None:
    #         self.match.player2.previous_opponents = []
            
    #     # rajoute chess_id de l'adversaire dans la liste des adversaires précédents
    #     # print(self.match.player1.previous_opponents)
    #     # print(self.match.player2.previous_opponents)
    #     self.match.player1.previous_opponents.append(self.match.player2.chess_id)
    #     self.match.player2.previous_opponents.append(self.match.player1.chess_id)
        
        
    #     return ([asdict(self.match.player1), self.match.player1.points], [asdict(self.match.player2), self.match.player2.points])
    #     # return [asdict(self.match.player1), asdict(self.match.player2)]

    
        
    # def run_match(self):
    #     self.get_match_result()
    #     updated_players = self.get_players_points_and_opponent_chess_id()

    #     # Update the players' scores in the tournament list
    #     for player in updated_players:
    #         for tournament_player in self.tournament.players:
    #             if player['chess_id'] == tournament_player.chess_id:
    #                 tournament_player.points = player['points']
    #                 tournament_player.previous_opponents = player['previous_opponents']

    #     self.display_match_result()

    
    # def run_match(self):
    #     self.get_match_result()
    #     self.get_players_points_and_opponent_chess_id()
    #     self.match_view.display_match_result(self.match)
    def run_match(self):
            self.get_match_result()
            self.get_players_points_and_opponent_chess_id()  
            self.match_view.display_match_result(self.match) 
            return deepcopy(self.match.player1), deepcopy(self.match.player2)
        
        
        
# match_view = MatchView()


# player_controller = PlayerController()
# match = Match(player1=player_controller.create_player(), player2=player_controller.create_player())


# match_controller = MatchController(match, match_view)
# match_controller.run_match()