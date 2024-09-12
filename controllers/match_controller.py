import sys
import os

# Relative path
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

from copy import deepcopy
from views.match_view import MatchView
from models.match import Match


class MatchController:
    def __init__(self, match, match_view):
        self.match = match
        self.match_view = match_view

    def get_players_points_and_opponent_chess_id(self):
        """Met à jour les points des joueurs et ajoute l'identifiant de l'adversaire
        à la liste des adversaires précédents."""
        result_of_match = self.get_match_result()

        if result_of_match == "1":
            self.match.player1.points += 1
            self.match.player2.points += 0
        elif result_of_match == "2":
            self.match.player2.points += 1
            self.match.player1.points += 0
        elif result_of_match == "0":
            self.match.player1.points += 0.5
            self.match.player2.points += 0.5

        # Initialiser la liste des adversaires précédents si elle n'existe pas
        if self.match.player1.previous_opponents is None:
            self.match.player1.previous_opponents = []
        if self.match.player2.previous_opponents is None:
            self.match.player2.previous_opponents = []

        # Ajouter l'identifiant de l'adversaire à la liste des adversaires précédents
        self.match.player1.previous_opponents.append(self.match.player2.chess_id)
        self.match.player2.previous_opponents.append(self.match.player1.chess_id)

    def get_match_result(self):
        """Obtient le résultat du match."""
        if self.match.result is None:
            self.match.result = self.match_view.input_match_result(self.match)
        return self.match.result

    def run_match(self):
        """Exécute le match et met à jour les informations des joueurs."""
        self.get_match_result()
        self.get_players_points_and_opponent_chess_id()
        self.match_view.display_match_result(self.match)
        return deepcopy(self.match.player1), deepcopy(self.match.player2)
