import os
import sys

# Relative path
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

from all_models.match import Match
from all_controllers.match_controller import MatchController
from all_views.match_view import MatchView
from all_models.round import Round
from all_models.player import Player
from all_views.player_view import PlayerView
from datetime import datetime
from random import shuffle
from copy import deepcopy


class RoundController:
    def __init__(self, round):
        self.round = round

    def generate_pairings(self, players):
        """Génère les paires de joueurs pour un round."""
        pairings = []
        # Trier les joueurs par points (ordre décroissant)
        players_sorted = sorted(players, key=lambda x: x.points, reverse=True)

        while len(players_sorted) > 1:
            player1 = players_sorted.pop(0)
            for i, player2 in enumerate(players_sorted):
                # Vérifier que les joueurs ne se sont pas déjà affrontés
                if player2.chess_id not in player1.previous_opponents:
                    pairings.append((player1, player2))
                    players_sorted.pop(i)
                    break
            else:
                # Si aucun adversaire n'est trouvé, prendre le premier joueur restant
                player2 = players_sorted.pop(0)
                pairings.append((player1, player2))

        return pairings
