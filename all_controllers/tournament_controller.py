import os
import sys

# Relative path
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

from datetime import datetime
from copy import deepcopy
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

class TournamentController:

    def __init__(self, file_path):
        self.file_path = file_path
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()
        self.tournament = None
        self.initialize_tournament()

    def initialize_tournament(self):
        """Initialise le tournoi en fonction du choix de l'utilisateur."""
        choice = self.tournament_view.prompt_for_action()
        if choice == "1":
            self.create_tournament()
        elif choice == "2":
            self.load_tournament_from_json()
        else:
            print("Invalid choice. Please restart the program and choose a valid option.")
            sys.exit(1)

    def create_tournament(self):
        """Crée un nouveau tournoi et ajoute des joueurs."""
        name, location, start_date, end_date, total_players, num_rounds, description = self.tournament_view.get_tournament_details()
        self.tournament = Tournament(name, location, start_date, end_date, total_players, num_rounds, description)
        self.add_players_to_tournament()
        self.save_tournament_to_json()

    def load_players_to_tournament_from_file(self):
        """Charge les joueurs à partir d'un fichier et les ajoute au tournoi."""
        if self.is_tournament_full():
            return
        file_path = self.player_view.get_file_path()
        players = Player.load_players_from_file(file_path)
        for player_data in players:
            if self.is_tournament_full():
                break
            player = Player(**player_data)
            if not self.is_player_in_tournament(player):
                self.tournament.add_player(player)
            else:
                print(f"Player {player.name} is already in the tournament.")
        self.save_tournament_to_json()

    def add_players_to_tournament(self):
        """Ajoute des joueurs au tournoi en fonction du choix de l'utilisateur."""
        while True:
            if self.is_tournament_full():
                print("Le tournoi est complet. Impossible d'ajouter plus de joueurs.")
                break
            choice = self.tournament_view.input_players()
            if choice == "1":
                chess_id = self.player_view.get_player_chess_id()
                player_data = {"chess_id": chess_id}
                player = Player.player_exists(player_data)
                if player:
                    player_instance = Player(**player)
                    if not self.is_player_in_tournament(player_instance):
                        self.tournament.add_player(player_instance)
                        print("Joueur ajouté au tournoi")
                    else:
                        print("Joueur déjà dans le tournoi")
                else:
                    print("Joueur non trouvé")
            elif choice == "2":
                player_controller = PlayerController()
                new_player = player_controller.create_player()
                if not self.is_player_in_tournament(new_player):
                    self.tournament.add_player(new_player)
                else:
                    print("Joueur déjà dans le tournoi")
            elif choice == "3":
                self.load_players_to_tournament_from_file()
            else:
                print("Choix invalide")
        self.save_tournament_to_json()

    def save_tournament_to_json(self):
        """Sauvegarde le tournoi dans un fichier JSON."""
        if self.tournament:
            self.tournament.tournament_to_json()

    def load_tournament_from_json(self):
        """Charge un tournoi à partir d'un fichier JSON."""
        file_path = self.tournament_view.get_file_path()
        self.tournament = Tournament.load_from_json(file_path)

    def is_tournament_full(self):
        """Vérifie si le tournoi est complet."""
        return len(self.tournament.players) >= int(self.tournament.total_players)

    def is_player_in_tournament(self, player):
        """Vérifie si un joueur est déjà dans le tournoi."""
        return any(p.chess_id == player.chess_id for p in self.tournament.players)

    def run_rounds(self):
        """Exécute les rounds du tournoi."""
        for i in range(int(self.tournament.num_rounds)):
            round = Round("Round " + str(i + 1), str(datetime.now()), None)
            round_controller = RoundController(round)
            pairings = round_controller.generate_pairings(self.tournament.players)

            if not pairings:
                print(f"Plus de pairs disponibles pour Round {i + 1}.")
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
            self.tournament.add_round(round)
            self.save_tournament_to_json()